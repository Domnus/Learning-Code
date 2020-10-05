#include <Keypad.h>

const byte numLin = 4;
const byte numCol = 4;

char keymap[numLin][numCol] =
    {
        {'1', '2', '3', 'A'},
        {'4', '5', '6', 'B'},
        {'7', '8', '9', 'C'},
        {'*', '0', '#', 'D'},
};

byte linPinos[numLin] = {11, 10, 9, 8};
byte colPinos[numCol] = {7, 6, 5, 4};

Keypad teclado = Keypad(makeKeymap(keymap), linPinos, colPinos, numLin, numCol);

char tecla;

char senhaCorreta[] = "1234";

void setup()
{
    pinMode(2, OUTPUT);
    Serial.begin(9600);
}

void loop()
{
    int i;
    char senha[4];
    char key = teclado.getKey();
    
    if (key != NO_KEY)
    {
        senha[i] = key;
        Serial.print(senha);
        i++;
    }

    if (i == 3)
    {
        if (senhaCorreta[0] == senha[0] && senhaCorreta[1] == senha[1] && senhaCorreta[2] == senha[2] && senhaCorreta[3] == senha[4])
        {
            digitalWrite(2, HIGH);
            Serial.print("Senha Correta!");
            delay(1000);
        }
        else
        {
            digitalWrite(2, LOW);
            Serial.print("Senha Incorreta!");
            delay(1000);
        }
    }
    Serial.print(senha);
}