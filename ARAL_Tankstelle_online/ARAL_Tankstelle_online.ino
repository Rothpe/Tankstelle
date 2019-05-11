#include <SPI.h>
#include <Wire.h>
#include <Adafruit_SSD1306.h>
#include <Adafruit_GFX.h>



// OLED display TWI address
#define OLED_ADDR   0x3C


Adafruit_SSD1306 display(-2);

#if (SSD1306_LCDHEIGHT != 64)
#error("Height incorrect, please fix Adafruit_SSD1306.h!");
#endif

void setup() {
  // initialize with the I2C addr 0x3C / mit I2C-Adresse 0x3c initialisieren
  
  display.begin(SSD1306_SWITCHCAPVCC, OLED_ADDR);
  display.clearDisplay();
  display.display();
  display.setTextColor(WHITE);
  display.setTextSize(2);
  display.display(); //Peter - Update Display with set values
  display.setRotation(3);                                                                                                                                                                                                                                                                                                                                                     
  
  
  // random start seed / zufälligen Startwert für Random-Funtionen initialisieren
  randomSeed(analogRead(0));
  
  // start serial port at 9600 bps:
  Serial.begin(9600);
  while (!Serial) {  
    // wait for serial port to connect. Needed for native USB port only
  };
  
  Serial.println("startup complete");
}


void clearLCD() {
  display.clearDisplay();
  display.display();
}

void writeToLCD(String caption, String valString) {
  caption.trim();

  if(caption.equals("Super E10")){
  	 Serial.println("printing value for Super E10: "+ valString);
	 display.setCursor(0, 0);//e.g. row 1
     display.setTextSize(2);
     display.print(valString.substring(0, 4));
     display.setTextSize(1);
     display.print(valString.substring(4, 5));
     display.display();
  }
  if(caption.equals("Super E5")){
  	 Serial.println("printing value for Super E5: "+ valString);
	 display.setCursor(0, 23);//e.g. row 2
     display.setTextSize(2);
     display.print(valString.substring(0, 4));
     display.setTextSize(1);
     display.print(valString.substring(4, 5));
     display.display();
  }
  if(caption.equals("ARAL Ultimate 102")){
  	 Serial.println("printing value for ARAL Ultimate 102: "+ valString);
	 display.setCursor(0, 46);//e.g. row 3
     display.setTextSize(2);
     display.print(valString.substring(0, 4));
     display.setTextSize(1);
     display.print(valString.substring(4, 5));
     display.display();
  }
  if(caption.equals("Diesel")){
     Serial.println("printing value for Diesel: "+ valString);
   display.setCursor(0, 69);//e.g. row 4
     display.setTextSize(2);
     display.print(valString.substring(0, 4));
     display.setTextSize(1);
     display.print(valString.substring(4, 5));
     display.display();
  }
  if(caption.equals("ARAL Ultimate Diesel")){
     Serial.println("printing value for ARAL Ultimate Diesel: "+ valString);
   display.setCursor(0, 92);//e.g. row 5
     display.setTextSize(2);
     display.print(valString.substring(0, 4));
     display.setTextSize(1);
     display.print(valString.substring(4, 5));
     display.display();
  }
  if(caption.equals("Autogas")){
     Serial.println("printing value for Autogas: "+ valString);
   display.setCursor(0, 115);//e.g. row 46
     display.setTextSize(2);
     display.print(valString.substring(0, 4));
     display.setTextSize(1);
     display.print(valString.substring(4, 5));
     display.display();
  }
}


String input;
void loop() {
  input = Serial.readStringUntil('\n');
  input.trim();
  
  if(input.length() > 0) {
    if (input == "#") {
      Serial.println("reset LCD");
      //Start new Dataset
      clearLCD();

    } else {
      int indexDelimiter = input.indexOf(':');
      if(indexDelimiter != -1) {
            String caption = input.substring(0, indexDelimiter);
            caption.trim();
            
            String valString = input.substring(indexDelimiter + 1);
            valString.trim();
            
            //double val = valString.toDouble();
            
            writeToLCD(caption, valString);
      } else {
        Serial.println("cannot process input: "+ input);
      }
    }
  }
}
