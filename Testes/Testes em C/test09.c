
#include <Keypad.h>
#include <Password.h>

Password password = Password("4317"); //password to unlock box, can be changed

const byte ROWS = 4; //4 rijen
const byte COLS = 3; //3 kolommen
char keys[ROWS][COLS] = {
    {'1', '2', '3'},
    {'4', '5', '6'},
    {'7', '8', '9'},
    {'*', '0', '#'},

};
byte rowPins[ROWS] = {10, 9, 8, 7}; //connect to 4567
byte colPins[COLS] = {6, 5, 4};     //connect to 8910
Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

void setup()
{
    Serial.begin(9600);
    Serial.write(254);
    Serial.write(0x01);
    delay(200);
    pinMode(A0, OUTPUT);                  //buzzer1
    pinMode(13, OUTPUT);                  //relay1(lade open)
    pinMode(11, OUTPUT);                  //relay2 (volgende puzzel aan)
    pinMode(12, OUTPUT);                  //relay 3 (morse ledjes)
    keypad.addEventListener(keypadEvent); //add an event listener for this keypad
}

void loop()
{

    keypad.getKey();
}
void keypadEvent(KeypadEvent eKey)
{
    switch (keypad.getState())
    {
    case PRESSED:

        Serial.print("Enter: ");
        Serial.println(eKey);
        digitalWrite(A0, HIGH); //buzzer on
        delay(10);
        digitalWrite(A0, LOW); //buzzer off

        Serial.write(254);

        switch (eKey)
        {
        case '#':
            checkPassword();
            delay(1);
            break;

        case '*':
            password.reset();
            delay(1);
            break;

        default:
            password.append(eKey);
            delay(1);
        }
    }
}
void checkPassword()
{

    if (password.evaluate())
    { //if password is right open box

        Serial.println("Accepted");
        Serial.write(254);
        delay(10);
        digitalWrite(A0, HIGH); //turn BUZZER on
        digitalWrite(13, HIGH); //turn RELAY on
        digitalWrite(11, HIGH); //turn RELAY on
        digitalWrite(12, HIGH); //morse ledjes uit
        delay(2000);            //wait 2 seconds
        digitalWrite(A0, LOW);  // turn BUZZER off
        delay(3600000);         //wait 5 seconds
    }
    else
    {
        Serial.println("Denied"); //if passwords wrong keep box locked
        Serial.write(254);
        delay(10);
        digitalWrite(A0, HIGH); //turn on
        delay(300);             //wait 0,3 seconds
        digitalWrite(A0, LOW);  //turn off
        delay(300);             //wait 0,3 seconds
        digitalWrite(A0, HIGH); //turn on
        delay(300);             //wait 0,3 seconds
        digitalWrite(A0, LOW);  //turn off
        delay(300);             //wait 0,3 seconds
        digitalWrite(A0, HIGH); //turn on
        delay(300);             //wait 0,3 seconds
        digitalWrite(A0, LOW);  //turn off
        delay(300);             //wait 0,3 seconds
        password.reset();
    }
}
