# Class A Transistor Amplifier Bias Optimization Program

## This Python program is designed to run on the TI-84 Plus CE Python Edition Calculator

### Current Release

* Version 1.0

### Description

This Python program is a faithful implementation of the Class A transistor amplifier bias optimization method described in an article written by _Ward J. Helms_ that was published in the 8 August 1974 edition of _Electronics_. After choosing a suitable bipolar transistor type and regulated power-supply voltage (Vcc), the user enters requested values from the transistor's datasheet to determine the optimal values for **_R1_**, **_R2_**, **_RL_**, and **_RE_**.

### Features

* The user can choose to run the article's example, or enter their own transistor's values.
* In addition to calculating **_R1_**, **_R2_**, **_RL_**, and **_RE_**, the prgram also calculates the minimum power gain (_Ap_) in dB and minimum signal power (_Ps_) in mW.

### Background

I am an electrical engineer by education and growing up I was fascinated with programmable scientific calculators manufactured during the mid-1970’s to the mid-1980’s, especially those from Hewlett Packard and Texas Instruments. For some of these programmable calculators, there were electrical engineering solution books or program ‘pacs’ available, and I remember coming across a program for the HP 67 scientific calculator that implemented a method for determining the optimal resistor values in a Class A transistor amplifier. A copy of this article is in the **References** folder. The method it followed was originally published in an article written by _Ward J. Helms_ where he describes the mathematical formulas needed to perform this optimization. Since it involves performing iterative calculations, it was a perfect application for a programmable calculator at that time.

More recently, I decided to implement this method in Python on a TI-84 Plus CE Python edition calculator that I had acquired. It seemed like a good way to test out the capabilities of this calculator. And now that I have a working version, I decided to make it available for anyone that might be interested.

Enjoy!
