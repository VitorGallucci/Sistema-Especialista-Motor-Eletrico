# Relatório do Sistema Especialista para Diagnóstico e Manutenção de Motores Elétricos

## 1. Objetivo
Este projeto desenvolve um sistema especialista para diagnóstico e manutenção preditiva
de motores elétricos. Implementado em Python, o sistema utiliza uma base de
conhecimento para identificar problemas comuns no motor e fornecer recomendações
específicas de manutenção com base nos sintomas informados.

## 2. Equipamento e Sintomas
Equipamento: Motor Elétrico Industrial
Sintomas Considerados:
- Temperatura Excessiva
- Vibração Excessiva
- Ruído Anômalo
- Redução de Velocidade
- Falta de Torque
- Oscilações na Corrente Elétrica

## 3. Diagnósticos e Recomendações
O sistema usa uma base de regras com três diagnósticos principais e suas respectivas
recomendações:
1. Desgaste dos Rolamentos- Recomendação: Lubrifique ou substitua os rolamentos.
2. Sobrecarga Elétrica - Recomendação: Verifique a carga elétrica e ajuste, se necessário.
3. Desgaste do Enrolamento - Recomendação: Inspecione e substitua o enrolamento, se
necessário.

## 4. Exemplos de Resultados
Exemplo 1
- Sintomas Informados: Temperatura Excessiva, Oscilações na Corrente Elétrica, Redução
de Velocidade
- Diagnóstico: Sobrecarga Elétrica
- Recomendação: Verifique a carga elétrica no motor e ajuste se necessário. Certifique-se
de que o motor não está sobrecarregado.
Explicação: A combinação desses sintomas indica que o motor está possivelmente
operando com uma carga excessiva, resultando em superaquecimento e instabilidade
elétrica.
Exemplo 2
- Sintomas Informados: Vibração Excessiva, Ruído Anômalo
- Diagnóstico: Desgaste dos Rolamentos
- Recomendação: Verifique e lubrifique os rolamentos. Substitua-os se houver sinais de
desgaste.
Explicação: Vibrações e ruídos anormais são sinais típicos de desgaste nos rolamentos, o
que pode afetar a estabilidade do motor.
Exemplo 3
- Sintomas Informados: Temperatura Excessiva, Falta de Torque
- Diagnóstico: Desgaste do Enrolamento
- Recomendação: Inspecione o enrolamento para detectar desgaste ou danos e substitua,
se necessário.
Explicação: A falta de torque e o superaquecimento sugerem problemas no enrolamento,
prejudicando o desempenho do motor.

## 5. Conclusão
O sistema especialista diagnosticou corretamente os problemas mais prováveis com base
nos sintomas e forneceu recomendações apropriadas para manutenção. Com o uso de
técnicas da Indústria 4.0 como os sistemas especialistas que estamos estudando, isso
pode otimizar a manutenção preditiva e reduzir tempos de inatividade.