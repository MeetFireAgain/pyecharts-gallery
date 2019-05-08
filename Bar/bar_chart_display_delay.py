import pyecharts.options as opts
from pyecharts.charts import Bar

"""
Gallery 使用 pyecharts 1.0.0
参考地址: https://www.echartsjs.com/examples/editor.html?c=bar-animation-delay

目前无法实现的功能:

1、动画延迟效果暂时没有加入到代码中
"""

category = ["类目{}".format(i) for i in range(0, 100)]
red_bar = [
    0,
    -8.901463875624668,
    -17.025413764148556,
    -24.038196249566663,
    -29.66504684804471,
    -33.699527649688676,
    -36.00971978255796,
    -36.541005056170455,
    -35.31542466107655,
    -32.427752866005996,
    -28.038563739693934,
    -22.364693082297347,
    -15.667600860943732,
    -8.240217424060843,
    -0.3929067389459173,
    7.560799717904647,
    15.318054209871054,
    22.599523033552096,
    29.16065418543528,
    34.800927952557615,
    39.37074152590451,
    42.77569739999406,
    44.97819140223978,
    45.99632376477021,
    45.900279829731865,
    44.806440199911805,
    42.86957840395034,
    40.2735832137877,
    37.22119936652441,
    33.92331243435557,
    30.588309963978517,
    27.412031986865767,
    24.56878097935778,
    22.203796820272576,
    20.427519715115604,
    19.311867685884827,
    18.888649906111855,
    19.150128087782186,
    20.051630602288828,
    21.516023200879346,
    23.439750867099516,
    25.700091656548704,
    28.163208735293757,
    30.692553648214542,
    33.1571635093161,
    35.439407573791215,
    37.44177367693234,
    39.09234039030659,
    40.34865356244595,
    41.19981246258526,
    41.66666666666667,
    41.80012531240646,
    41.67768039516203,
    41.39834040182826,
    41.07625507973403,
    40.833382300579814,
    40.79160029175877,
    41.06470032034727,
    41.75070457358366,
    42.924940903672564,
    44.63427081999565,
    46.89281122872821,
    49.679416561286956,
    52.93709961387478,
    56.574470884754874,
    60.46917221906629,
    64.47317623531558,
    68.41972346252496,
    72.1315793340836,
    75.43021771943799,
    78.14548044723074,
    80.12522637371026,
    81.24447108408411,
    81.41353029256493,
    80.58471628367427,
    78.75719600392792,
    75.97969924353211,
    72.35086229880064,
    68.01710226438443,
    63.16803467673056,
    58.029567166714706,
    52.854918421647554,
    47.91391949819902,
    43.48104807503482,
    39.82272085822884,
    37.18442111754884,
    35.778264289169215,
    35.77160292258658,
    37.27724241244461,
    40.345781666728996,
    44.96051012913295,
    51.035187614675685,
    58.41491053964701,
    66.8801325453253,
    76.15376513468516,
    85.91114110149952,
    95.79248672571518,
    105.41742429574506,
    114.40092042993717,
    122.37001313784816,
]
blue_bar = [
    -50,
    -47.18992898088751,
    -42.54426104547181,
    -36.290773900754886,
    -28.71517529663627,
    -20.146937097399626,
    -10.94374119697364,
    -1.4752538113770308,
    7.893046603320797,
    16.81528588241657,
    24.979206795219028,
    32.11821023962515,
    38.02096119056733,
    42.53821720798438,
    45.58667093073836,
    47.14973738101559,
    47.275355710354944,
    46.07100702178889,
    43.6962693226927,
    40.35333240268025,
    36.275975292575026,
    31.71756381888028,
    26.938653692729076,
    22.194784893913152,
    17.725026430574392,
    13.741778696752679,
    10.422266555457615,
    7.902063853319403,
    6.270884006107842,
    5.570756810898967,
    5.796594266992678,
    6.899033489892203,
    8.7893381290192,
    11.346045936704996,
    14.42297348773613,
    17.858132851517098,
    21.483081596548438,
    25.132218074866262,
    28.651548555679597,
    31.906490373810854,
    34.788333671419466,
    37.21906041552118,
    39.154309232933485,
    40.58437366457342,
    41.5332247510366,
    42.05565130942339,
    42.23270781895,
    42.165745792772285,
    41.969375711588256,
    41.76375960543808,
    41.66666666666667,
    41.7857343479728,
    42.21136481847887,
    43.01065209435119,
    44.22268037417866,
    45.855461823273586,
    47.88469584957917,
    50.25443606443524,
    52.879650371477126,
    55.650558977584225,
    58.43853958732492,
    61.10330341815434,
    63.500974294013034,
    65.49264961151306,
    66.95298925309743,
    67.77836838841961,
    67.89414332224722,
    67.26061575374229,
    65.87733853082335,
    63.785482681031894,
    61.068077697490004,
    57.84804048526095,
    54.284018163297375,
    50.564180830851214,
    46.89820707575337,
    43.50780217852947,
    40.616171775045245,
    38.4369379107128,
    37.16302649485318,
    36.95607267600796,
    37.93688225696513,
    40.17745279877072,
    43.694998595987045,
    48.44834150353593,
    54.33692802801367,
    61.20261650152743,
    68.83425165632042,
    76.97491319735354,
    85.33159602026458,
    93.58695857541488,
    101.4126683297632,
    108.48378461530217,
    114.49355390682695,
    119.16795429637915,
    122.27931702317058,
    123.65837448506679,
    123.20413594805603,
    120.89107255501017,
    116.7731992576505,
    110.98476877890735,
]


(
    Bar(init_opts=opts.InitOpts(width="1600px", height="800px"))
    .add_xaxis(xaxis_data=category)
    .add_yaxis(
        series_name="bar", yaxis_data=red_bar, label_opts=opts.LabelOpts(is_show=False)
    )
    .add_yaxis(
        series_name="bar2",
        yaxis_data=blue_bar,
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="柱状图动画延迟"),
        xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=False)),
        yaxis_opts=opts.AxisOpts(
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
    )
    .render("bar_chart_display_delay.html")
)
