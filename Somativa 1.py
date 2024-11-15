from unidecode import unidecode

class MotorDiagnostico:
    def __init__(self):
        # Base de conhecimento com os diagnósticos e sintomas associados
        self.base_conhecimento = {
            "Rolamentos Desgastados": {
                "sintomas": ["vibracao excessiva", "ruido anomalo", "reducao de velocidade"],
                "recomendacao": "Verifique e lubrifique os rolamentos. Substitua-os se houver sinais de desgaste ou folga excessiva."
            },
            "Sobrecarga Elétrica": {
                "sintomas": ["temperatura excessiva", "oscilacoes na corrente eletrica", "reducao de velocidade"],
                "recomendacao": "Verifique a carga elétrica no motor e ajuste se necessário. Certifique-se de que o motor não está sobrecarregado."
            },
            "Desgaste do Enrolamento": {
                "sintomas": ["temperatura excessiva", "oscilacoes na corrente eletrica", "falta de torque"],
                "recomendacao": "Inspecione o enrolamento do motor para detectar sinais de desgaste ou danos. Substitua o enrolamento, se necessário."
            }
        }

    def normalizar_texto(self, texto):
        # Converte para minúsculas e remove acentos
        return unidecode(texto.lower())

    def diagnosticar(self, sintomas):
        # Normaliza os sintomas fornecidos pelo usuário
        sintomas_normalizados = [self.normalizar_texto(sintoma) for sintoma in sintomas]

        # Diagnóstico com base nos sintomas
        diagnostico_mais_provavel = None
        maior_contagem = 0

        for diagnostico, info in self.base_conhecimento.items():
            # Conta o número de sintomas que coincidem com os sintomas associados ao diagnóstico
            contagem = sum(1 for sintoma in sintomas_normalizados if sintoma in info["sintomas"])
            # Se a contagem for maior que a maior contagem encontrada até agora, atualiza o diagnóstico mais provável
            if contagem > maior_contagem:
                maior_contagem = contagem
                diagnostico_mais_provavel = diagnostico

        # Retorna o diagnóstico mais provável e sua recomendação, ou None se não houver diagnóstico
        if diagnostico_mais_provavel:
            recomendacao = self.base_conhecimento[diagnostico_mais_provavel]["recomendacao"]
            return diagnostico_mais_provavel, recomendacao
        else:
            return None, None


if __name__ == "__main__":
    # Instancia o sistema especialista
    diagnostico_motor = MotorDiagnostico()

    # Pergunta ao usuário os sintomas observados
    print("Informe os sintomas observados no motor, separando-os por vírgula.")
    print("Opções: Temperatura Excessiva, Vibração Excessiva, Ruído Anômalo, Redução de Velocidade, Falta de Torque, Oscilações na Corrente Elétrica")
    entrada_usuario = input("Sintomas: ")

    # Processa os sintomas fornecidos
    sintomas_observados = [sintoma.strip() for sintoma in entrada_usuario.split(",")]

    # Realiza o diagnóstico com base nos sintomas
    diagnostico, recomendacao = diagnostico_motor.diagnosticar(sintomas_observados)

    # Exibe o diagnóstico e a recomendação
    if diagnostico:
        print(f"\nDiagnóstico: {diagnostico}")
        print(f"Recomendação: {recomendacao}")
    else:
        print("\nNão foi possível identificar um diagnóstico específico com os sintomas fornecidos.")
