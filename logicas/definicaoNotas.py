import services.notas as nota
import controles.controleJogo as controle
import classes.jogo as jogo


k = 0

def calcularNotas(adversarioData, nivelJogo, dataJogo, campeonato, categoria, referencia, tempoTotalJogo, atleta, posicao, gol, finaGol,
                           finaFora, finaBloq, assistFina, assistGol, chanceClara, bloqFina, intercep, desarmeCerto, desarmeErrado, dribleCerto,
                           perdaBola, passeCerto, passeErrado, passeVertical, passeVerticalErrado, passeLongo, passeLongoErrado, cruzamento, 
                           cruzamentoErrado, vitoriaAereo, derrotaAereo, MCD, MCO, tempoEmJogo, MCDTotal, MCOTotal, intercepTotal):
        
        limiteCriacao = 0
        limiteConfront = 0
        limiteComplet = 0

        if(posicao == 'ZAGUEIRO'):
                limiteCriacao = 30
                limiteConfront = 75
                limiteComplet = 45
        if(posicao == 'LATERAL'):
                limiteCriacao = 50
                limiteConfront = 65
                limiteComplet = 35
        if(posicao == 'VOLANTE'):
                limiteCriacao = 50
                limiteConfront = 65
                limiteComplet = 35
        if(posicao == 'MEIO CAMPO'):
                limiteCriacao = 65
                limiteConfront = 55
                limiteComplet = 30
        if(posicao == 'EXTREMA'):
                limiteCriacao = 65
                limiteConfront = 55
                limiteComplet = 30
        if(posicao == 'CENTROAVANTE'):
                limiteCriacao = 70
                limiteConfront = 50
                limiteComplet = 30

        valoresConfront = nota.confront(posicao, passeCerto, passeErrado, passeVertical, passeVerticalErrado, passeLongo, 
                                        passeLongoErrado, desarmeCerto, desarmeErrado, dribleCerto, perdaBola, vitoriaAereo, 
                                        derrotaAereo, cruzamento, cruzamentoErrado)
        valoresCriacoes = nota.criacoes(posicao, gol, finaGol, finaFora, finaBloq, chanceClara, assistFina, assistGol)
        valoresComplet = nota.complet(posicao, MCD, MCO, intercep, bloqFina, MCDTotal, MCOTotal, intercepTotal)
        

        criacoes = (valoresCriacoes.assistFina + valoresCriacoes.assistGol + valoresCriacoes.chanceClara + valoresCriacoes.finaBloq
        + valoresCriacoes.finaFora + valoresCriacoes.finaGol) 

        confront = (valoresConfront.Ncruzamento + valoresConfront.NpasseLongo + valoresConfront.NpasseVertical + valoresConfront.Ndrible
        + valoresConfront.Ndesarme + valoresConfront.NvitoriaAereo)

        complet = valoresComplet.Nbloqfina + valoresComplet.Nintercep + valoresComplet.NMCD + valoresComplet.NMCO 

        if(criacoes >= limiteCriacao):
                criacoes = limiteCriacao
        
        criacoes += valoresCriacoes.gol

        if(confront >= limiteConfront):
                confront = limiteConfront
        
        if(complet >= limiteComplet):
                complet = limiteComplet

        notaFinal = criacoes + confront + complet

        if (notaFinal >= 100):
                notaFinal = 10
        else:
                notaFinal = notaFinal / 10

        nota_ofensiva = (valoresCriacoes.assistFina + valoresCriacoes.assistGol + valoresCriacoes.chanceClara + valoresCriacoes.finaBloq
        + valoresCriacoes.finaFora + valoresCriacoes.finaGol + valoresConfront.Ncruzamento + valoresConfront.NpasseLongo 
        + valoresConfront.NpasseVertical + valoresConfront.Ndrible + valoresConfront.NvitoriaAereo + valoresComplet.NMCO)

        nota_defensiva = (valoresComplet.Nbloqfina + valoresComplet.Nintercep + valoresConfront.Ndesarme + valoresComplet.NMCD)
        
        
        controle.cadastrar(jogo.jogo(adversarioData, nivelJogo, dataJogo, campeonato, categoria, referencia, tempoTotalJogo,
                                        atleta, posicao, tempoEmJogo, gol, finaGol, finaFora, finaBloq, assistFina, assistGol,
                                        chanceClara, bloqFina, intercep, desarmeCerto, desarmeErrado, dribleCerto, perdaBola, 
                                        passeCerto, passeErrado, passeVertical, passeVerticalErrado, passeLongo, passeLongoErrado, 
                                        cruzamento, cruzamentoErrado, vitoriaAereo, derrotaAereo, MCD, MCO, round(notaFinal, 1), criacoes, 
                                        confront, complet, nota_ofensiva, nota_defensiva))