from typing import Tuple
import math

import torch
import torch.nn as nn

from models import Discriminator, Generator
from utils import generate_even_data, convert_float_matrix_to_int_list


def train(
    max_int: int = 128, #128
    batch_size: int = 20, #16
    training_steps: int = 1000, #500
    learning_rate: float = 0.001, #0.001
    print_output_every_n_steps: int = 200,
    ) -> Tuple[nn.Module]:
    """Trains the even GAN

    Args:
        max_int: The maximum integer our dataset goes to.  It is used to set the size of the binary
            lists
        batch_size: The number of examples in a training batch
        training_steps: The number of steps to train on.
        learning_rate: The learning rate for the generator and discriminator
        print_output_every_n_steps: The number of training steps before we print generated output

    Returns:
        generator: The trained generator model
        discriminator: The trained discriminator model
    """
    # Get the number of binary places needed to represent the maximum number
    input_length = int(math.log(max_int, 2))

    # Models
    generator = Generator(input_length)
    discriminator = Discriminator(input_length)

    # Optimizers
    generator_optimizer = torch.optim.Adam(generator.parameters(), lr=learning_rate)
    discriminator_optimizer = torch.optim.Adam(
        discriminator.parameters(), lr=learning_rate
    )

    # loss
    loss = nn.BCELoss()

    for i in range(training_steps):
        # zero the gradients on each iteration
        generator_optimizer.zero_grad()

        # Create noisy input for generator
        # Need float type instead of int
        noise = torch.randint(0, 2, size=(batch_size, input_length)).float()
        generated_data = generator(noise)
        # print(f"\n noise : \n {noise} \n")
        # print(f"\n generated_data : \n {generated_data} \n")

        # Generate examples of even real data
        true_labels, true_data = generate_even_data(max_int, batch_size=batch_size)
        true_labels = torch.tensor(true_labels).float()
        true_data = torch.tensor(true_data).float()
        # print(f"true_data: {true_data}")

        # Train the generator
        # We invert the labels here and don't train the discriminator because we want the generator
        # to make things the discriminator classifies as true.
        generator_discriminator_out = discriminator(generated_data)
        # to avoid /nn/modules/loss.py:498: UserWarning: Using a target size
        generator_discriminator_out = generator_discriminator_out.reshape(-1)
        #Calculate the loss from the discriminator’s output using labels as if the data were “real” instead of fake.
        generator_loss = loss(generator_discriminator_out, true_labels)
        # print(f"generator_loss: {generator_loss}")
        #Backpropagate the error through just the generator
        generator_loss.backward()
        generator_optimizer.step()


        # Train the discriminator on the true/generated data
        discriminator_optimizer.zero_grad()
        true_discriminator_out = discriminator(true_data)
        # to avoid /nn/modules/loss.py:498: UserWarning: Using a target size
        true_discriminator_out = true_discriminator_out.reshape(-1)
        # print(f"true_discriminator_out: {true_discriminator_out}")
        true_discriminator_loss = loss(true_discriminator_out, true_labels)
        # print(f"true_discriminator_loss: {true_discriminator_loss}")

        # add .detach() here think about this
        generator_discriminator_out = discriminator(generated_data.detach())
        # to avoid /nn/modules/loss.py:498: UserWarning: Using a target size
        generator_discriminator_out = generator_discriminator_out.reshape(-1)
        generator_discriminator_loss = loss(
            generator_discriminator_out, torch.zeros(batch_size)
        )
        # print(f"generator_discriminator_loss: {generator_discriminator_loss}")

        # Average the loss from steps one and two
        discriminator_loss = (
            true_discriminator_loss + generator_discriminator_loss
        ) / 2
        print(f"discriminator_loss: {discriminator_loss}")
        # Backpropagate the gradients through just the discriminator.
        discriminator_loss.backward()
        discriminator_optimizer.step()
        if i % print_output_every_n_steps == 0:
            print(f"{i} : {convert_float_matrix_to_int_list(generated_data)}")

    return generator, discriminator

if __name__ == "__main__":
    train()
