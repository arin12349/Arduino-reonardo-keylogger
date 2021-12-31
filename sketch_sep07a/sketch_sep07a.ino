#include <Keyboard.h>

char ch;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Keyboard.begin();
}
 
void loop() {
  // put your main code here, to run repeatedly:
  while (Serial.available() > 0){
    ch = Serial.read();
    if(ch == '1'){
      Keyboard.print(KEY_LEFT_ALT);
    }
    else if(ch == '2'){
      Keyboard.press(KEY_LEFT_SHIFT);
      delay(80);
      Keyboard.releaseAll();
    }
    else if(ch == '3'){
      Keyboard.press(KEY_DOWN_ARROW);
      delay(80);
      Keyboard.releaseAll();
    }
    else if(ch == '4'){
      Keyboard.press(KEY_LEFT_ARROW);
      delay(80);
      Keyboard.releaseAll();
    }
    else if(ch == '5'){
      Keyboard.press(KEY_RIGHT_ARROW);
      delay(80);
      Keyboard.releaseAll();
    }
    else if(ch == '6'){
      Keyboard.press(KEY_UP_ARROW);
      delay(80);
      Keyboard.releaseAll();
    }
    else{
      Keyboard.write(ch);
    }
  }
}
