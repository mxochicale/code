# R [#71](https://github.com/mxochicale/code/issues/71)
> R is a programming language for statistical computing and data visualization. It has been adopted in the fields of data mining, bioinformatics, and data analysis https://en.wikipedia.org/wiki/R_(programming_language).

See my [R Source Code Repository](https://github.com/mxochicale/r), I guess I would like to mention that I started using R in 2014 for [PhD thesis](https://github.com/mxochicale-phd/thesis).

## Installation 
```
bash installation.bash
#uninstall
#sudo apt-get remove r-base r-base-core  
```

## Test installation
```
R --version
#R version 4.4.0 (2024-04-24) -- "Puppy Cup"
```

## RStudio IDE for linux
* Download your IDE based on your OS https://posit.co/download/rstudio-desktop/
```bash
wget https://download1.rstudio.org/electron/jammy/amd64/rstudio-2025.09.1-401-amd64.deb -O rstudio-2025.09.1-401-amd64.deb

sudo apt-get install gdebi-core
sudo gdebi rstudio-2025.09.1-401-amd64.deb
```
* Launch it
```bash
rstudio
#2025.09.1 Build 401
```

## References
* https://cran.r-project.org/bin/linux/ubuntu/
