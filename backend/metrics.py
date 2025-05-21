from prometheus_client import Counter, Gauge, Info

UPLOAD_COUNT = Counter('upload_count', 'Count of uploads')
ANOMALY_COUNT = Counter('anomaly_count', 'Count of anomalies')

NOT_IN_ZONE = Gauge(
    'not_in_zone',
    'Indicator that a geometry fell outside its assigned zone (0 or 1)',
    ['zone_type', 'code']
)

LONG_CONN_PERCENT = Gauge(
    'long_connections_percentage',
    'Pourcentage de raccordements RA dont la longueur > 90 m'
)
LONG_CONN_CM_LENGTH = Gauge(
    'long_connections_cm_length',
    'Longueur des raccordements CM dépassant 500 mètres',
    ['cm_codeext']
)
CB_CAPAFO_EXCESS = Gauge(
    'cb_aerial_capacity_excess',
    'Capacité des câbles aériens dépassant 144 FO',
    ['cl_codeext']
)
PA_UMFTTH_EXCESS = Gauge(
    'pa_umftth_excess',
    'Valeur du µm FTTH dépassant 20 µm par PA',
    ['pcn_code']
)
CB_D1_LENGTH_EXCESS = Gauge(
    'cb_d1_length_excess',
    'Longueur des CB D1 dépassant 2100 mètres',
    ['cl_codeext']
)
PA_ON_ENEDIS_SUPPORT = Gauge(
    "pa_on_enedis_support",
    "PA superposé sur appui ENEDIS",
    ["pcn_code", "latitude", "longitude"],
)