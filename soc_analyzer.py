print("Mini SOC Analyzer iniciado") 

# Lista de eventos para análise
eventos = [
    {"timestamp":"2025-03-10 09:00:10","ip":"192.168.1.10","usuario":"admin","evento":"login","status":"sucesso","porta":22,"servico":"ssh"},
    {"timestamp":"2025-03-10 09:01:12","ip":"192.168.1.15","usuario":"admin","evento":"login","status":"falha","porta":22,"servico":"ssh"},
    {"timestamp":"2025-03-10 09:01:15","ip":"192.168.1.15","usuario":"admin","evento":"login","status":"falha","porta":22,"servico":"ssh"},
    {"timestamp":"2025-03-10 09:01:17","ip":"192.168.1.15","usuario":"admin","evento":"login","status":"falha","porta":22,"servico":"ssh"},
    {"timestamp":"2025-03-10 09:02:03","ip":"10.0.0.25","usuario":"-","evento":"scan_porta","status":"detectado","porta":80,"servico":"http"},
    {"timestamp":"2025-03-10 09:02:05","ip":"10.0.0.25","usuario":"-","evento":"scan_porta","status":"detectado","porta":443,"servico":"https"},
    {"timestamp":"2025-03-10 09:03:20","ip":"172.16.0.5","usuario":"maria","evento":"login","status":"sucesso","porta":443,"servico":"webapp"},
    {"timestamp":"2025-03-10 09:04:33","ip":"8.8.8.8","usuario":"-","evento":"acesso_externo","status":"permitido","porta":80,"servico":"web"}
]

def contar_eventos(lista_eventos):
    pass

def identificar_bruteforce(lista_eventos):
    pass

def identificar_scanners(lista_eventos):
    pass

def listar_ips_unicos(lista_eventos):
    pass

def gerar_relatorio(lista_eventos):
    print("=== MINI SOC ANALYZER ===\n")
    print(f"Total de eventos analisados: {len(lista_eventos)}")
    # As outras funções serão chamadas aqui depois
    pass

if __name__ == "__main__":
    gerar_relatorio(eventos)