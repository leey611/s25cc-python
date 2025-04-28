# Environment setup
This guide will setup `sardine` in a python virtual environment.

## Reference
- [Sardine official docs: Installation](https://sardine.raphaelforment.fr/installation.html)

## Install SuperCollider
- Download [SuperCollider](https://supercollider.github.io/)
- Open SuperCollider, type `Quarks.install("SuperDirt")` and hit `Shift + Enter`

To make sure if SuperCollider is running properly:
- Type `s.boot;` and hit `Shift + Enter` to start the server
- Type `{ SinOsc.ar(440) * 0.2 }.play;` and hit `Shift + Enter` to test the sound
- Type `s.freeAll;` and hit `Shift + Enter` to stop the sound

## Install Sardine
Create a `main.py` file, and run the following command in your terminal:
```
pip install sardine-system
```
[reference](https://sardine.raphaelforment.fr/installation/macos.html#installing-sardine)

## Install Sardine Web
Sardine Web is the actual editor where you write our code.
```
pip install sardine-web
```

## Check if Sardine and Sardine Web are installed properly
[reference](https://sardine.raphaelforment.fr/installation/post_install_checkup.html#can-you-run-sardine-and-sardine-web)
- run `sardine` in your terminal to see if it shows [this](https://sardine.raphaelforment.fr/getting_started/starting.html)
- run `sardine-web` to see if the web editor pops up. Keep this running to write code.

## Code evaluation
[reference](https://sardine.raphaelforment.fr/getting_started/code_evaluation.html)

In sardine web, type `Pa >> d('bd cp')` and hit `Shift + Enter` on the line of code to hear the sound.
To stop the sound, on another line, type `silence()` and hit `Shift + Enter` on the line of code .