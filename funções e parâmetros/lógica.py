'''
Funções: 

-> sequência de instruções que computa um ou mais resultados que chamamos de parâmetros.

parâmetros:

-> Um	conjunto de	parâmetros	consiste em	uma	lista com nenhum ou	mais elementos	que	podem	ser
obrigatórios ou	 opcionais.	

Também	podemos	criar	nossas próprias funções. Por exemplo, quando queremos calcular a razão	do
espaço pelo tempo,	podemos	definir uma função	recebendo estes parâmetros:
				f(espaco,	tempo) =	espaco/tempo
Essa razão do espaço pelo tempo	é o que chamamos de velocidade média na	física. Podemos então
dar este nome a nossa função:
				velocidade(espaco,	tempo) = espaco/tempo
Se um carro  percorreu uma distância de 100 metros em 20 segundos, podemos calcular	 sua
velocidade média:
				velocidade(100, 20) = 100/20	= > 
                                          >>> 5 m/s
Podemos definir funções	como essa da velocidade média. Para definirmos  uma função no Python, utilizamos o comando '' def '':
				def velocidade(espaco,	tempo):
								pass
Logo após o ''def'' vem o nome	da função, e entre parênteses vêm os seus parâmetros. Uma função
também tem um escopo	e um bloco de	instruções onde colocamos os cálculos,	onde estes devem seguir
a identação padrão	do Python (4	espaços	a	direita).
Como nossa função ainda não faz	nada, utilizamos a palavra chave ''pass'' para dizer ao interpretador
que	definiremos os	cálculos depois. A palavra pass não é	usada apenas em	funções, podemos usar	em 
qualquer bloco de comandos	como nas instruções if,	while e for , por exemplo



'''

def velocidade( espaço, tempo): # definindo a função 
    v = espaço/tempo # cálculo
    print(f' Sua velocidade: {v} m/s') # mostrar o resultado

# Atribuindo valores e chamando a função
espaço = 100  # valor em metros
tempo = 10  # valor em segundos

velocidade(espaço, tempo)  # chamando a função com os valores atribuídos