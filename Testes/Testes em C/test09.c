int ldr = 0;

void setup()
{
    Serial.begin(9600);
    pinMode(A0, INPUT);
    pinMode(2, OUTPUT);
}

void loop()
{
    ldr = analogRead(A0);
    Serial.print("Valor LDR = ");
    Serial.println(ldr);
    // testar com ldr =500
    if (ldr < 500)
    {
        digitalWrite(2, HIGH);
    }
    else
    {
        digitalWrite(2, LOW);
    }
    
}