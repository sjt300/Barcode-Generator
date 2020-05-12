# ITF-Barcode-Generator
Using TKinter, produces up to 20 IFT barcodes for 9 digit codes

Introduction and reasons for it
- This is my first github upload so very much open to feedback.
- I created this program as I work in a supermarket where we use 9 digit numbers to represent each product.
- The issue I wanted to resolve is that, having upgraded company software and PDAs, it has broken some of the usability and efficency and I was sure that creating this program would(in the long run obviously!) save time.
- The reason I believe this to be the case is that people in my section of the supermarkert industry (stock controllers), are typically numpad wizards(!) and can type in numbers like you've never seen purely because we do it so much on a day-to-day.  Doing the same thing on a touch screen pda is a very much lengthier process due to not having a 'feel' for the buttons/keys therefore having to look a lot closer at the screen (taking your eye off the numbers) and more mistakes made whilst trying not to look at the screen for sake of efficiency.
-Also, with our new PDAs, instead of the older horizontal line-lazer scanner, now there is some sort of scanner that scans a significantly larger area which leads to picking up other barcodes if there are nearby (there frequently are if scanning barcodes off paper for some of our count routines) so had to adpat this into the usability of the program.

Instructions
-Type a valid 9 dig number into the Entry field (valid: begins with '0' len = 9) after the 9th digit, the program automatically extracts the input
- In it's current build it will only generate barcodes for a 9 digit number.  It adds on 5 zeroes to the end to make it 14 digits as this is acceptable for our scanners to read the important bit of the barcode
-After the first barcode it created, for subsequent entries, it will show a blacked out rectangle with the new 9 dig number displayed next to it.  This is so that when scanning commences, the PDA will not pick up other barcodes as described in the issues faced above
-To advance to the next barcode or, if already advanced and the need arose to go back, the <Up> and <down> arrow keys are used
- The "Clear Screen" button should be pretty self-evident

Future intended Improvements
-Code: Having been fairly inexperienced with Classes/modules, I didn't use any.  For the next build I would use a seperate module to build the functions.  Also more comments required.
-If I can find applications for other businesses that use ITF barcodes (off the top of my head, possbily outer-case-codes or delivery barcodes) I could tweak it to accept longer barcodes and also introduce accepting numbers that don't begin with '0'.
-Change rectangles to lines in Tkinter canvas as while develpoing new build, lines seem to work alot better with coordinates
