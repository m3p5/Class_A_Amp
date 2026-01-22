# Class A Transistor Amplifier Bias Optimization Program

## This Python program is designed to run on the TI-84 Plus CE Python Edition Calculator

### Current Release

* Version 2.0

### Description

This Python program is a faithful implementation of the Class A transistor amplifier bias optimization method described in an article titled "_Designing class A amplifiers to meet specified tolerances_" written by _Ward J. Helms_ that was published in the 8 August 1974 edition of _Electronics_. A copy of this article is located [here](https://github.com/m3p5/Class_A_Amp/blob/main/References/Designing_Class_A_Amps-Electronics_1974-08-08.pdf). This program gives the user the option of running the example in the article or entering values from their own transistor's datasheet to determine the optimal values for **_R1_**, **_R2_**, **_RL_**, and **_RE_**. The data sheet for the Texas Instruments TIS98 NPN transistor used in the article is located [here](https://github.com/m3p5/Class_A_Amp/blob/main/References/TIS94_thru_TIS99_Datasheet.pdf).

### Features

* The user can choose to run the article's example, or enter their own transistor's values.
* In addition to calculating **_R1_**, **_R2_**, **_RL_**, and **_RE_**, the prgram also calculates the minimum power gain (_Ap_) in dB, minimum signal power (_Ps_) in mW, and the maximum transistor junction temperature (_Tjmax_) in °C.
* The final optimzed set of resistor values are choosen from the nearest [E24](https://en.wikipedia.org/wiki/E_series_of_preferred_numbers#E24_subsets) standard resistor values.

### Installation Notes

All three .py files (_BIAS84.py_, _BIASDEFA.py_, and _BIASDEFB.py_) need to be transfered to your TI-84 Plus CE Python calculator using [TI Connect CE](https://education.ti.com/en/products/computer-software/ti-connect-ce-sw) software. _BIAS84.py_ is the main Python program, and it calls a function in _BIASDEFA.py_ which in turn calls a function in _BIASDEFB.py_. I found that combining all of the code into one monolithic Python file was too much for the Python interpreter on this calculator (it would fail due to using too much memory), but I was successful in getting it to run by breaking it into three files.

### Background

I am an electrical engineer by education and growing up I was fascinated with scientific programmable calculators manufactured during the mid-1970’s to the mid-1980’s, especially those from Hewlett Packard and Texas Instruments.

For some of these programmable calculators, there were electrical engineering solution books or program ‘pacs’ available, and I remember coming across a program for the HP 67 scientific programmable calculator that implemented a method for determining the optimal resistor values in a Class A transistor amplifier. The method it followed was originally published in the article referenced in the **Description** above where _Ward J. Helms_ describes the mathematical formulas needed to perform this optimization. Since it involves performing iterative mathematical calculations, it was a perfect application for a scientific programmable calculator at that time.

More recently, I decided to implement this method in Python on my TI-84 Plus CE Python calculator. It seemed like a good way to explore and test the Python programming capabilities of this calculator. And now that I have a working version, I decided to make it available for anyone that might be interested.

Enjoy!
