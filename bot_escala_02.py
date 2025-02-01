import datetime, pandas, locale

locale.setlocale(locale.LC_ALL, 'pt_BR')


def novo_datetime(dia, mes, ano): return datetime.date(ano, mes, dia)


def delta(n_dias): return datetime.timedelta(days=n_dias)


def formato_do_modulo(dia): return dia.strftime('%Y-%m-%d')


def formato_bra(dia): return dia.strftime('%d-%m-%Y')


def dia_semana(dia): return dia.strftime('%A')


da, db, dab, ta, tb = 'A', 'B', 'A ou B', 'Turno A', 'Turno B'
futuro = 60
hoje = datetime.date.today() + delta(8)
primeiro_a = novo_datetime(19, 12, 2024)
data_futuro = hoje + delta(futuro)
escala = pandas.DataFrame(
    {
        'Data': [],
        'Dia da semana': [],
        'Disponibilidade': []
    }
).astype(str)
escala = escala.set_index('Data')


def __chk_servico(datetime_dia):
    dia = formato_bra(datetime_dia)
    dia_da_semana = dia_semana(datetime_dia)
    try:
        escala.loc[[dia, ]]
    except KeyError:
        d = datetime_dia - primeiro_a
        resto = int(d.days % 4)
        if resto == 1: escala.loc[dia, ['Dia da semana', 'Disponibilidade']] = [dia_da_semana, tb]
        if resto == 2: escala.loc[dia, ['Dia da semana', 'Disponibilidade']] = [dia_da_semana, db]
        if resto == 3: escala.loc[dia, ['Dia da semana', 'Disponibilidade']] = [dia_da_semana, da]
        if resto == 0: escala.loc[dia, ['Dia da semana', 'Disponibilidade']] = [dia_da_semana, ta]
        return escala.loc[[dia, ]]


def mostra_agenda():
    __update_servicos()
    print(escala)


def __update_servicos():
    for i in range(futuro):
        __chk_servico(hoje + delta(i))


def mostra_disponiveis():
    __update_servicos()
    print(escala[escala['Disponibilidade'] == 'A'])
    print()
    print(escala[escala['Disponibilidade'] == 'B'])


print('\n\n```Disponível para tirar serviço nos dias:\n')
mostra_disponiveis()
print(f'\nR$ 200, TURNO B\n'
      f'R$ 150, TURNO A\n\n'
      f'SD 32711 PASSOS - MAT 308.935-0-6\n'
      f'CEL/WHATS: (85) 9 9157-9721\n'
      f'PRIVADO: https://wa.me/5585991579721\n'
      f'LINK DE PERMUTA: https://tinyurl.com/permutaBtl'
      f'```')