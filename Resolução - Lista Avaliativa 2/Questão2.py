anoshumanos = int(input("Digite o número de anos humanos: "))

if anoshumanos > 0:
    if anoshumanos <= 2:
        if anoshumanos == 1:
            anoscaninostotal = anoshumanos * 10.5
            print(anoshumanos, "ano humano equivale a", anoscaninostotal, "anos caninos.")
        else:
            anoscaninostotal = anoshumanos * 10.5
            print(anoshumanos, "anos humanos equivalem a", anoscaninostotal, "anos caninos.")
    else:
        anoscaninostotal = ((anoshumanos - 2) * 4) + 21
        print(anoshumanos, "anos humanos equivalem a", anoscaninostotal, "anos caninos.")
else:
    print("ERRO: digite um número inteiro positivo.")