import streamlit as st
def aproveitamento(x, y, z):
    if(x == 0):
        aproveitamento = 0
            
    else:
        aproveitamento = (((100 / ((x + y) / x)) * z) / 100)

    return aproveitamento
 
def calculaComplet(x, y, z):
    calculaComplet = (y / z)

    if(x < calculaComplet):
        calculaComplet = 0
    else:
        calculaComplet = z

    return calculaComplet

def calculaIntercep(x, y, z):
    #st.write(x)
    #st.write(y)
    if(x== 0):
        calculaIntercep = 0
    else:
        calculaIntercep = ((x / y) * 100)

        if (calculaIntercep > z):
            calculaIntercep = z
    
    return calculaIntercep

class criacoes:
    def __init__(self, posicao, gol, finaGol, finaFora, finaBloq, chanceClara, assistFina, assistGol):
        st.write(posicao)
        if posicao == 'ZAGUEIRO':   
            self.gol = 20 * gol
            self.finaGol = 4 * finaGol
            self.finaFora = 2 * finaFora
            self.finaBloq = 0.5 * finaBloq
            self.chanceClara = 4 * chanceClara
            self.assistFina = 2.5 * assistFina
            self.assistGol = 7 * assistGol
        
        if posicao == 'LATERAL':
            self.gol = 25 * gol
            self.finaGol = 5 * finaGol
            self.finaFora = 2.5 * finaFora
            self.finaBloq = 1.5 * finaBloq
            self.chanceClara = 9 * chanceClara
            self.assistFina = 5 * assistFina
            self.assistGol = 12 * assistGol
        
        if posicao == 'VOLANTE':
            self.gol = 25 * gol
            self.finaGol = 6.5 * finaGol
            self.finaFora = 3.5 * finaFora
            self.finaBloq = 2 * finaBloq
            self.chanceClara = 8 * chanceClara
            self.assistFina = 5 * assistFina
            self.assistGol = 10 * assistGol

        if posicao == 'MEIO CAMPO':
            self.gol = 25 * gol
            self.finaGol = 9 * finaGol
            self.finaFora = 4.5 * finaFora
            self.finaBloq = 2.5 * finaBloq
            self.chanceClara = 9.5 * chanceClara
            self.assistFina = 7.5 * assistFina
            self.assistGol = 12 * assistGol

        if posicao == 'EXTREMA':
            self.gol = 25 * gol
            self.finaGol = 10 * finaGol
            self.finaFora = 5.5 * finaFora
            self.finaBloq = 3 * finaBloq
            self.chanceClara = 9.5 * chanceClara
            self.assistFina = 6 * assistFina
            self.assistGol = 11 * assistGol

        if posicao == 'CENTROAVANTE':
            self.gol = 30 * gol
            self.finaGol = 14 * finaGol
            self.finaFora = 9 * finaFora
            self.finaBloq = 4.5 * finaBloq
            self.chanceClara = 7.5 * chanceClara
            self.assistFina = 5 * assistFina
            self.assistGol = 10 * assistGol

class confront:
    def __init__(self, posicao, passeCerto, passeErrado,  passeVertical, passeVerticalErrado, passeLongo, passeLongoErrado, desarmeCerto,
                desarmeErrado, dribleCerto, perdaBola, vitoriaAereo, derrotaAereo, cruzamento, cruzamentoErrado):
        if posicao == 'ZAGUEIRO': 
            self.NpasseVertical = aproveitamento(passeVertical, passeVerticalErrado, 8)
            self.NpasseLongo = aproveitamento(passeLongo, passeLongoErrado, 7)
            self.Ndrible = aproveitamento (dribleCerto, perdaBola, 1)
            self.Ndesarme = aproveitamento(desarmeCerto, desarmeErrado, 15)
            self.NvitoriaAereo = aproveitamento(vitoriaAereo, derrotaAereo, 17)
            self.Ncruzamento = aproveitamento(cruzamento, cruzamentoErrado, 1)
            self.Npasses = aproveitamento(passeCerto, passeErrado, 6) 
                  
        if posicao == 'LATERAL':
            self.NpasseVertical = aproveitamento(passeVertical, passeVerticalErrado, 1.5)
            self.NpasseLongo = aproveitamento(passeLongo, passeLongoErrado, 0.5)
            self.Ndrible = aproveitamento (dribleCerto, perdaBola, 6)
            self.Ndesarme = aproveitamento(desarmeCerto, desarmeErrado, 11)
            self.NvitoriaAereo = aproveitamento(vitoriaAereo, derrotaAereo, 9)
            self.Ncruzamento = aproveitamento(cruzamento, cruzamentoErrado, 17)
            self.Npasses = aproveitamento(passeCerto, passeErrado, 5)  
        
        if posicao == 'VOLANTE': 
            self.NpasseVertical = aproveitamento(passeVertical, passeVerticalErrado, 9.5)
            self.NpasseLongo = aproveitamento(passeLongo, passeLongoErrado, 5.5)
            self.Ndrible = aproveitamento (dribleCerto, perdaBola, 3.5)
            self.Ndesarme = aproveitamento(desarmeCerto, desarmeErrado, 12)
            self.NvitoriaAereo = aproveitamento(vitoriaAereo, derrotaAereo, 9.5)
            self.Ncruzamento = aproveitamento(cruzamento, cruzamentoErrado, 2.5)
            self.Npasses = aproveitamento(passeCerto, passeErrado, 7.5) 

        if posicao == 'MEIO CAMPO': 
            self.NpasseVertical = aproveitamento(passeVertical, passeVerticalErrado, 10)
            self.NpasseLongo = aproveitamento(passeLongo, passeLongoErrado, 4)
            self.Ndrible = aproveitamento (dribleCerto, perdaBola, 10)
            self.Ndesarme = aproveitamento(desarmeCerto, desarmeErrado, 4)
            self.NvitoriaAereo = aproveitamento(vitoriaAereo, derrotaAereo, 2.5)
            self.Ncruzamento = aproveitamento(cruzamento, cruzamentoErrado, 6.5)
            self.Npasses = aproveitamento(passeCerto, passeErrado, 8)

        if posicao == 'EXTREMA':
            self.NpasseVertical = aproveitamento(passeVertical, passeVerticalErrado, 7)
            self.NpasseLongo = aproveitamento(passeLongo, passeLongoErrado, 2)
            self.Ndesarme = aproveitamento (dribleCerto, perdaBola, 18)
            self.Ndrible = aproveitamento(desarmeCerto, desarmeErrado, 4)
            self.NvitoriaAereo = aproveitamento(vitoriaAereo, derrotaAereo, 1)
            self.Ncruzamento = aproveitamento(cruzamento, cruzamentoErrado, 8)
            self.Npasses = aproveitamento(passeCerto, passeErrado, 5)  

        if posicao == 'CENTROAVANTE':
            self.NpasseVertical = aproveitamento(passeVertical, passeVerticalErrado, 4)
            self.NpasseLongo = aproveitamento(passeLongo, passeLongoErrado, 3)
            self.Ndrible = aproveitamento (dribleCerto, perdaBola, 12.5)
            self.Ndesarme = aproveitamento(desarmeCerto, desarmeErrado, 3)
            self.NvitoriaAereo = aproveitamento(vitoriaAereo, derrotaAereo, 12.5)
            self.Ncruzamento = aproveitamento(cruzamento, cruzamentoErrado, 4)
            self.Npasses = aproveitamento(passeCerto, passeErrado, 6)  

class complet:
    def __init__(self, posicao, MCD, MCO, intercep, 
                 bloqFina, MCDTotal, MCOTotal, intercepTotal):
        if posicao == 'ZAGUEIRO':   
            self.NMCD = calculaComplet(MCD, MCDTotal, 10)
            self.NMCO = calculaComplet(MCO, MCOTotal, 8)
            self.Nintercep = calculaIntercep(intercep, intercepTotal, 22)
            self.Nbloqfina = 10 * bloqFina
        
        if posicao == 'LATERAL':
            self.NMCD = calculaComplet(MCD, MCDTotal, 11.5)
            self.NMCO = calculaComplet(MCO, MCOTotal, 10)
            self.Nintercep = calculaIntercep(intercep, intercepTotal, 8.5)
            self.Nbloqfina = 5 * bloqFina
        
        if posicao == 'VOLANTE':
            self.NMCD = calculaComplet(MCD, MCDTotal, 11.5)
            self.NMCO = calculaComplet(MCO, MCOTotal, 10)
            self.Nintercep = calculaIntercep(intercep, intercepTotal, 8.5)
            self.Nbloqfina = 5 * bloqFina

        if posicao == 'MEIO CAMPO':
            self.NMCD = calculaComplet(MCD, MCDTotal, 8.5)
            self.NMCO = calculaComplet(MCO, MCOTotal, 11.5)
            self.Nintercep = calculaIntercep(intercep, intercepTotal, 5)
            self.Nbloqfina = 4 * bloqFina

        if posicao == 'EXTREMA':
            self.NMCD = calculaComplet(MCD, MCDTotal, 8.5)
            self.NMCO = calculaComplet(MCO, MCOTotal, 11.5)
            self.Nintercep = calculaIntercep(intercep, intercepTotal, 5)
            self.Nbloqfina = 4 * bloqFina

        if posicao == 'CENTROAVANTE':
            self.NMCD = calculaComplet(MCD, MCDTotal, 7.5)
            self.NMCO = calculaComplet(MCO, MCOTotal, 9.5)
            self.Nintercep = calculaIntercep(intercep, intercepTotal, 3)
            self.Nbloqfina = 2 * bloqFina