#include "gaussian_multi_gpu_rdma.h"

void generateLinearSystem(unsigned char *A, unsigned char* B, unsigned char* x, int rowCount, int columnCount, int percent)
{

    unsigned long int row, col;
    int dice;

    percent = (percent*64)/100;

    for(row = 0; row < rowCount; row++)
    {
        for(col = 0; col < columnCount; col++)
        {
            dice = (((rand() >> 8) & 63)+1);
            if(dice <= percent)
                A[row*columnCount+col] = (unsigned char) 1;
            else
                A[row*columnCount+col] = (unsigned char) 0;
        }
    }

    for(col = 0; col < columnCount; col++)
    {
        x[col] = (unsigned char)((rand() >> 8) % 2);
    }

    for(row = 0; row < rowCount; row++)
    {
        B[row] = 0;
        for(col = 0; col < columnCount; col++)
        {
            B[row] ^= (A[row*columnCount+col] & x[col]);
        }
    }

    return;
}

int writeVectorToFile(const char* filename, unsigned char* vector, int length)
{
    FILE *fp;
    int col;

    fp = fopen(filename, "w");
    
    if(fp == NULL)
    {
        printf("Failed to open file '%s' for writing.\n", filename);
        return -1;
    }

    for(col = 0; col < length; col++)
    {
        
        fprintf(fp, "%u\n", (unsigned int) vector[col]);
    }

    fclose(fp);
    return 0;
}


void packLinearSystem(elemtype* packedAB, unsigned char* A, unsigned char* B, int rowCount, int columnCount)
{
    int i, j, k;
    int packedColumnCount = intCeilDiv((columnCount + 1), PACK_SIZE); // One extra column for B
    elemtype temp;

    long int index, packIndex, bitIndex;

    for(i = 0; i < rowCount; i++)
    {
        for(j = 0; j < packedColumnCount; j++)
        {
            resetElement(&temp);
            for(k = 0; k < PACK_SIZE; k++)
            {
                if((j*PACK_SIZE + k) < columnCount) 
                {
                    index = (long int)i * columnCount + (j*PACK_SIZE + k);
                    if(A[index])
                    {
                        // temp |= (1 << k);
                        setElementBit(&temp, k);
                    }
                }
                
            }
            index = (long int)i * packedColumnCount + j;
            packedAB[index] = temp;
        }
    }

    for(i = 0; i < rowCount; i++)
    {
        index = i * packedColumnCount + (packedColumnCount - 1); // B is embedded as last column
        bitIndex = columnCount % PACK_SIZE;
        if(B[i])
        {
            // packedAB[index] |= (1 << bitIndex);
            setElementBit(&packedAB[index], bitIndex);
        }
    }
}

void unpackLinearSystem(unsigned char* A, unsigned char* B, elemtype* packedAB, int rowCount, int columnCount)
{
    int i, j, k;
    int packedColumnCount = intCeilDiv((columnCount + 1), PACK_SIZE); // One extra column for B
    elemtype temp;
    long int index, packIndex, bitIndex;

    for(i = 0; i < rowCount; i++)
    {
        for(j = 0; j < packedColumnCount; j++)
        {
            index = (long int)i * packedColumnCount + j;
            temp = packedAB[index];
            for(k = 0; k < PACK_SIZE; k++)
            {
                if(j*PACK_SIZE + k < columnCount)
                {
                    index = (long int)i * columnCount + j*PACK_SIZE + k;
                    // A[index] = (temp >> k) & 1;
                    A[index] = getElementBit(&temp, k);
                }
            }
        }
    }
    for(i = 0; i < rowCount; i++)
    {
        index = i * packedColumnCount  + packedColumnCount - 1; // B is embedded as last column
        bitIndex = columnCount % PACK_SIZE;
        // B[i] = (unsigned char) ((packedAB[index] >> bitIndex) & 1);
        B[i] = getElementBit(&packedAB[index], bitIndex);
    }
}

void transposeMatrixCPU(elemtype *transposeA, elemtype *A, int rowCount, int columnCount)
{
    int row, col;
    long int index1, index2;
    for(row = 0; row < rowCount; row++)
    {
        for(col = 0; col < columnCount; col++)
        {
            index1 = (long int)col*rowCount + row;
            index2 = (long int)row*columnCount + col;
            transposeA[index1] = A[index2];
        }
    }
}

void writeLinearSystemFromFile(const char* filename, unsigned char* matrixA, unsigned char* B, int rowCount, int columnCount)
{
    int row, col;
    FILE* fp;
    long int index;

    fp = fopen(filename, "w");

    if(fp == NULL)
    {
        printf("Failed to open file %s for writing.\n", filename);
        return;
    }
    for(row = 0; row < rowCount; row++)
    {
        for(col = 0; col < columnCount; col++)
        {
            index = (long int)row*columnCount + col;
            fprintf(fp, "%u, ", (unsigned int)matrixA[index]);
        }
        fprintf(fp, "%u\n", B[row]);
    }
    fclose(fp);
}

int backsubstitution(unsigned char* matrixA, unsigned char* B, unsigned char* x, int number_of_equations, int number_of_variables)
{
    int row, col, var;
    int* pivoteRowIndex;
    long int index;

    memset(x, 0, sizeof(unsigned char)*number_of_variables);

    pivoteRowIndex = (int*) malloc(sizeof(int)*number_of_equations);

    for(row = 0; row < number_of_equations; row++)
    {
        pivoteRowIndex[row] = -1;
    }

    for(row = 0; row < number_of_equations; row++)
    {
        for(col = 0; col < number_of_variables; col++)
        {
            index = (long int)row*number_of_variables+col;
            if(matrixA[index] != 0)
                break;
        }
        if(col != number_of_variables)
        {
            // printf("Row %d is pivot for col %d\n", row, col);
            pivoteRowIndex[col] = row;
        }
        else
        {
             // printf("Row %d is NULL\n", row);
        }
    }

    for(var = number_of_variables - 1; var >= 0; var--)
    {
        if(pivoteRowIndex[var] == -1)
        {
            printf("backsubstitution failed at %d\n", var);
            break;
        }
        row = pivoteRowIndex[var];
        x[var] = B[row];
        for(col = var+1; col < number_of_variables; col++)
        {
            index = (long int)row*number_of_variables+col;
            x[var] ^= (matrixA[index] & x[col]);
        }
    }

    free(pivoteRowIndex);
    return 0;
}
