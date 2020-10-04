#include <Keypad.h>

const byte numLin = 4;
const byte numCol = 4;
char senha[4] = "1234";
char password[4];

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

void setup()
{
    pinMode(2, OUTPUT);
    Serial.begin(9600);
}

void loop()
{
    for (int i = 0; i < 4; i++)
    {
        tecla = teclado.getKey();
        password = password + tecla;
        i++;
    }
    if (password == senha)
    {
        digitalWrite(2, HIGH);
    }
}