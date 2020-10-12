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
int i = 0;
char senhaCorreta[4] = {'1','2','3','4'};
char senha[4] = {'*','*','*','*'};

void reset()
{
  i = 0;
  senha[0] = '*';
  senha[1] = '*';
  senha[2] = '*';
  senha[3] = '*';
}

char senhaCorreta[] = "1234";

void setup()
{
    pinMode(2, OUTPUT);
  	pinMode(3, OUTPUT);
    Serial.begin(9600);
}

void loop()
{
    
    char key = teclado.getKey();
    
    if (key != NO_KEY && i != 4)
    {
        senha[i] = key;
        Serial.println(senha);
      	Serial.println(i);
        i++;
    }

    if (i == 3)
    {
        if (senhaCorreta[0] == senha[0] && senhaCorreta[1] == senha[1] && senhaCorreta[2] == senha[2] && senhaCorreta[3] == senha[3])
        {
          	Serial.println("Senha Correta!");
            digitalWrite(2, HIGH);
            delay(2000);
            reset();
        }
        else
        {
            
         	digitalWrite(2, LOW);
          	delay(2000);
          	reset();
        }
    }
   
}
