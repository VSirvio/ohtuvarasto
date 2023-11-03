import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_virheellinen_tilavuus_olion_luonnissa(self):
        varasto = Varasto(-3.7)
        self.assertAlmostEqual(varasto.tilavuus, 0)

    def test_virheellinen_saldo_olion_luonnissa(self):
        varasto = Varasto(2.03, -501.0)
        self.assertAlmostEqual(varasto.saldo, 0)

    def test_negatiivisen_maaran_lisays_varastoon(self):
        saldo_alussa = self.varasto.saldo
        self.varasto.lisaa_varastoon(-0.7)
        self.assertAlmostEqual(self.varasto.saldo, saldo_alussa)

    def test_lisaa_varastoon_liikaa(self):
        self.varasto.lisaa_varastoon(10.01)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_ota_varastosta_negatiivinen_maara(self):
        otettu_maara = self.varasto.ota_varastosta(-0.01)
        self.assertAlmostEqual(otettu_maara, 0)

    def test_ota_varastosta_liikaa(self):
        otettu_maara = self.varasto.ota_varastosta(113.9)
        self.assertAlmostEqual(otettu_maara, 0)

    def test_muunnos_merkkijonoksi(self):
        mjono = self.varasto.__str__()
        self.assertEqual(mjono, "saldo = 0, vielä tilaa 10")
