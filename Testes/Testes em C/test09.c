#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 10, 5, 4, 3, 2);
int ldr = 0;
int backLight = 13;
int s0, s1, s2, s3;

void setup()
{
    pinMode(backLight, OUTPUT);
    pinMode(A0, INPUT);
    pinMode(9, INPUT_PULLUP);
    pinMode(8, INPUT_PULLUP);
    pinMode(7, INPUT_PULLUP);
    pinMode(6, INPUT_PULLUP);

    digitalWrite(backLight, HIGH);
    lcd.begin(16, 2);
    lcd.clear();
}

void loop()
{
    s0 = digitalRead(6);
    s1 = digitalRead(7);
    s2 = digitalRead(8);
    s3 = digitalRead(9);

    ldr = analogRead(A0);
    lcd.clear();

    if (ldr > 500)
    {
        lcd.setCursor(5, 0);
        lcd.print("Estamos");
        lcd.setCursor(4, 1);
        lcd.print("Atendendo!");
    }
    else
    {
        if (s0 == LOW && s1 == HIGH && s2 == LOW && s3 == HIGH)
        {
            lcd.setCursor(4, 0);
            lcd.print("A porta");
            lcd.setCursor(2, 1);
            lcd.print("foi destravada");
        }
        else
        {
            lcd.setCursor(4, 0);
            lcd.print("A porta");
            lcd.setCursor(2, 1);
            lcd.print("foi travada");
        }
        
    }
    delay(1000);
}