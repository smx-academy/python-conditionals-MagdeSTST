""" Напишете програма која ќе прочита големина на агли во триаголник, 
    да се провери дали може да се формира триаголник со тие агли(збирот мора да биде 180) 
    и ако може да се формира триаголник да се провери каков триаголник може да се формира"""

α= int(input('Внеси го аголот α на триаголникот:'))

β= int(input('Внеси го аголот β на триаголникот:'))

γ= int(input('Внеси го аголот γ на триаголникот:'))

p_zbir = α + β + γ

if p_zbir == 180:
    print('Може да се формира триаголник')
    if α==90 or β==90 or γ==90:
        print('Триаголникот е правоаголен')
    if α<90 and β<90 and γ<90:
        print('Триаголникот е остроаголен')
    if α>90 or β>90 or γ>90:
        print('Триаголникот е тапоаголен')
else:
    print('Неможе да се формира триаголник, збирот на аглите е поголем од 180')        