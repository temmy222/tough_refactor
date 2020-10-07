# TOUGH-PLOTS

![Project Image](https://github.com/temmy222/tough_refactor/blob/master/images/Multi%20plot%20vs%20time.png)

> 

---

### Table of Contents

- [Description](#description)
- [How To Use](#how-to-use)
- [References](#references)
- [License](#license)
- [Author Info](#author-info)

---

## Description

These sets of scripts help to make plots from TOUGH softwares (TOUGH3, TMVOC and TOUGHREACT). The scripts can make 2D plots, single plots, multi plots ready for publications. The advantage of these scripts is the ease of usage and manipulation for specific needs.

#### Technologies

- Python

[Back To The Top](#read-me-template)

---

## How To Use
TOUGH-PLOTS is developed using Object Oriented Programming concepts. Installation is described below. 

It consists of a FileReadSingle class which reads in single files and does manipulations on those files to create plots. For plots involving multiple files, a FileReadMultiple class is provided. 

A simple use case for a line plot of pH against time with the time axis in days and the 106th grid block is shown in the example below.

Similar plots can be made for TOUGH3 and TMVOC.

#### Installation
Use of the code requires the installation of external python libraries Numpy and Pandas. To use created style sheet, please copy the 'mystyle' style sheet from the plotting package to the appropriate matplotlib directory. Otherwise, the code will default to the 'classic' style sheet.


#### Example

```html
    file_toughreact = r"insert_file_location"
    filetype_toughreact = 'kddconc.tec'
    testcodetoughreact = FileReadSingle("toughreact", file_toughreact, filetype_toughreact)
    testcodetoughreact.plotTime('pH', 106, format_of_date='day')
```
[Back To The Top](#read-me-template)

---

## References
[Back To The Top](#read-me-template)

I can be reached on tajayi3@lsu.edu for collaboration or more information on how to use.

---

## License

MIT License

Copyright (c) [2020] [Temitope Ajayi]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[Back To The Top](#read-me-template)

---

## Author Info

Temitope Ajayi is a Graduate Student at Louisiana State University


[Back To The Top](#read-me-template)
