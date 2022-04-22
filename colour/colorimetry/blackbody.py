"""
Blackbody - Planckian Radiator
==============================

Defines the objects to compute the spectral radiance of a planckian radiator
and its spectral distribution.

References
----------
-   :cite:`CIETC1-482004i` : CIE TC 1-48. (2004). APPENDIX E. INFORMATION ON
    THE USE OF PLANCK'S EQUATION FOR STANDARD AIR. In CIE 015:2004 Colorimetry,
    3rd Edition (pp. 77-82). ISBN:978-3-901906-33-6
"""

from __future__ import annotations

import numpy as np

from colour.colorimetry import (
    SPECTRAL_SHAPE_DEFAULT,
    SpectralDistribution,
    SpectralShape,
)
from colour.hints import Floating, FloatingOrArrayLike, FloatingOrNDArray
from colour.utilities import as_float_array

__author__ = "Colour Developers"
__copyright__ = "Copyright 2013 Colour Developers"
__license__ = "New BSD License - https://opensource.org/licenses/BSD-3-Clause"
__maintainer__ = "Colour Developers"
__email__ = "colour-developers@colour-science.org"
__status__ = "Production"

__all__ = [
    "CONSTANT_C1",
    "CONSTANT_C2",
    "CONSTANT_N",
    "planck_law",
    "blackbody_spectral_radiance",
    "sd_blackbody",
]

# 2 * math.pi * CONSTANT_PLANCK * CONSTANT_LIGHT_SPEED ** 2
CONSTANT_C1: float = 3.741771e-16

# CONSTANT_PLANCK * CONSTANT_LIGHT_SPEED / CONSTANT_BOLTZMANN
CONSTANT_C2: float = 1.4388e-2

CONSTANT_N: float = 1


def planck_law(
    wavelength: FloatingOrArrayLike,
    temperature: FloatingOrArrayLike,
    c1: Floating = CONSTANT_C1,
    c2: Floating = CONSTANT_C2,
    n: Floating = CONSTANT_N,
) -> FloatingOrNDArray:
    """
    Return the spectral radiance of a blackbody at thermodynamic temperature
    :math:`T[K]` in a medium having index of refraction :math:`n`.

    Parameters
    ----------
    wavelength
        Wavelength in meters.
    temperature
        Temperature :math:`T[K]` in kelvin degrees.
    c1
        The official value of :math:`c1` is provided by the Committee on Data
        for Science and Technology (CODATA) and is
        :math:`c1=3,741771x10.16\\ W/m_2` *(Mohr and Taylor, 2000)*.
    c2
        Since :math:`T` is measured on the International Temperature Scale,
        the value of :math:`c2` used in colorimetry should follow that adopted
        in the current International Temperature Scale (ITS-90)
        *(Preston-Thomas, 1990; Mielenz et aI., 1991)*, namely
        :math:`c2=1,4388x10.2\\ m/K`.
    n
        Medium index of refraction. For dry air at 15C and 101 325 Pa,
        containing 0,03 percent by volume of carbon dioxide, it is
        approximately 1,00028 throughout the visible region although
        *CIE 15:2004* recommends using :math:`n=1`.

    Returns
    -------
    :class:`numpy.floating` or :class:`numpy.ndarray`
        Radiance in *watts per steradian per square metre* (:math:`W/sr/m^2`).

    Notes
    -----
    -   The following form implementation is expressed in term of wavelength.
    -   The SI unit of radiance is *watts per steradian per square metre*
        (:math:`W/sr/m^2`).

    References
    ----------
    :cite:`CIETC1-482004i`

    Examples
    --------
    >>> planck_law(500 * 1e-9, 5500)  # doctest: +ELLIPSIS
    20472701909806.5...
    """

    l = as_float_array(wavelength)  # noqa
    t = as_float_array(temperature)

    p = ((c1 * n**-2 * l**-5) / np.pi) * (np.expm1(c2 / (n * l * t))) ** -1

    return p


blackbody_spectral_radiance = planck_law


def sd_blackbody(
    temperature: Floating,
    shape: SpectralShape = SPECTRAL_SHAPE_DEFAULT,
    c1: Floating = CONSTANT_C1,
    c2: Floating = CONSTANT_C2,
    n: Floating = CONSTANT_N,
) -> SpectralDistribution:
    """
    Return the spectral distribution of the planckian radiator for given
    temperature :math:`T[K]` with values in
    *watts per steradian per square metre per nanometer* (:math:`W/sr/m^2/nm`).

    Parameters
    ----------
    temperature
        Temperature :math:`T[K]` in kelvin degrees.
    shape
        Spectral shape used to create the spectral distribution of the
        planckian radiator.
    c1
        The official value of :math:`c1` is provided by the Committee on Data
        for Science and Technology (CODATA) and is
        :math:`c1=3,741771x10.16\\ W/m_2` *(Mohr and Taylor, 2000)*.
    c2
        Since :math:`T` is measured on the International Temperature Scale,
        the value of :math:`c2` used in colorimetry should follow that adopted
        in the current International Temperature Scale (ITS-90)
        *(Preston-Thomas, 1990; Mielenz et aI., 1991)*, namely
        :math:`c2=1,4388x10.2\\ m/K`.
    n
        Medium index of refraction. For dry air at 15C and 101 325 Pa,
        containing 0,03 percent by volume of carbon dioxide, it is
        approximately 1,00028 throughout the visible region although
        *CIE 15:2004* recommends using :math:`n=1`.

    Returns
    -------
    :class:`colour.SpectralDistribution`
        Blackbody spectral distribution with values in
        *watts per steradian per square metre per nanometer*
        (:math:`W/sr/m^2/nm`).

    Examples
    --------
    >>> from colour.utilities import numpy_print_options
    >>> with numpy_print_options(suppress=True):
    ...     sd_blackbody(5000)  # doctest: +ELLIPSIS
    SpectralDistribution([[   360.        ,   6654.2782706...],
                          [   361.        ,   6709.6052792...],
                          [   362.        ,   6764.8251215...],
                          [   363.        ,   6819.9330786...],
                          [   364.        ,   6874.9244898...],
                          [   365.        ,   6929.7947526...],
                          [   366.        ,   6984.5393232...],
                          [   367.        ,   7039.1537166...],
                          [   368.        ,   7093.6335071...],
                          [   369.        ,   7147.9743284...],
                          [   370.        ,   7202.1718736...],
                          [   371.        ,   7256.2218956...],
                          [   372.        ,   7310.1202073...],
                          [   373.        ,   7363.8626816...],
                          [   374.        ,   7417.4452515...],
                          [   375.        ,   7470.8639102...],
                          [   376.        ,   7524.1147113...],
                          [   377.        ,   7577.1937686...],
                          [   378.        ,   7630.0972565...],
                          [   379.        ,   7682.8214094...],
                          [   380.        ,   7735.3625224...],
                          [   381.        ,   7787.7169506...],
                          [   382.        ,   7839.8811097...],
                          [   383.        ,   7891.8514754...],
                          [   384.        ,   7943.6245836...],
                          [   385.        ,   7995.1970300...],
                          [   386.        ,   8046.5654705...],
                          [   387.        ,   8097.7266205...],
                          [   388.        ,   8148.6772551...],
                          [   389.        ,   8199.4142089...],
                          [   390.        ,   8249.9343757...],
                          [   391.        ,   8300.2347083...],
                          [   392.        ,   8350.3122185...],
                          [   393.        ,   8400.1639766...],
                          [   394.        ,   8449.7871113...],
                          [   395.        ,   8499.1788096...],
                          [   396.        ,   8548.3363163...],
                          [   397.        ,   8597.2569337...],
                          [   398.        ,   8645.9380216...],
                          [   399.        ,   8694.3769968...],
                          [   400.        ,   8742.5713329...],
                          [   401.        ,   8790.5185599...],
                          [   402.        ,   8838.2162638...],
                          [   403.        ,   8885.6620864...],
                          [   404.        ,   8932.8537251...],
                          [   405.        ,   8979.7889322...],
                          [   406.        ,   9026.4655149...],
                          [   407.        ,   9072.8813344...],
                          [   408.        ,   9119.0343064...],
                          [   409.        ,   9164.9223997...],
                          [   410.        ,   9210.5436366...],
                          [   411.        ,   9255.8960922...],
                          [   412.        ,   9300.9778938...],
                          [   413.        ,   9345.7872209...],
                          [   414.        ,   9390.3223045...],
                          [   415.        ,   9434.5814267...],
                          [   416.        ,   9478.5629206...],
                          [   417.        ,   9522.2651692...],
                          [   418.        ,   9565.6866057...],
                          [   419.        ,   9608.8257125...],
                          [   420.        ,   9651.6810212...],
                          [   421.        ,   9694.2511118...],
                          [   422.        ,   9736.5346124...],
                          [   423.        ,   9778.5301986...],
                          [   424.        ,   9820.2365935...],
                          [   425.        ,   9861.6525666...],
                          [   426.        ,   9902.7769336...],
                          [   427.        ,   9943.6085564...],
                          [   428.        ,   9984.1463416...],
                          [   429.        ,  10024.3892411...],
                          [   430.        ,  10064.3362510...],
                          [   431.        ,  10103.9864112...],
                          [   432.        ,  10143.3388051...],
                          [   433.        ,  10182.3925589...],
                          [   434.        ,  10221.1468414...],
                          [   435.        ,  10259.6008633...],
                          [   436.        ,  10297.7538768...],
                          [   437.        ,  10335.6051749...],
                          [   438.        ,  10373.1540914...],
                          [   439.        ,  10410.3999999...],
                          [   440.        ,  10447.3423137...],
                          [   441.        ,  10483.9804852...],
                          [   442.        ,  10520.3140051...],
                          [   443.        ,  10556.3424025...],
                          [   444.        ,  10592.0652439...],
                          [   445.        ,  10627.4821331...],
                          [   446.        ,  10662.5927104...],
                          [   447.        ,  10697.3966524...],
                          [   448.        ,  10731.8936712...],
                          [   449.        ,  10766.0835144...],
                          [   450.        ,  10799.9659640...],
                          [   451.        ,  10833.5408365...],
                          [   452.        ,  10866.8079821...],
                          [   453.        ,  10899.7672843...],
                          [   454.        ,  10932.4186594...],
                          [   455.        ,  10964.7620561...],
                          [   456.        ,  10996.7974551...],
                          [   457.        ,  11028.5248683...],
                          [   458.        ,  11059.9443388...],
                          [   459.        ,  11091.0559402...],
                          [   460.        ,  11121.8597759...],
                          [   461.        ,  11152.3559791...],
                          [   462.        ,  11182.5447121...],
                          [   463.        ,  11212.4261658...],
                          [   464.        ,  11242.0005596...],
                          [   465.        ,  11271.2681403...],
                          [   466.        ,  11300.2291822...],
                          [   467.        ,  11328.8839867...],
                          [   468.        ,  11357.2328813...],
                          [   469.        ,  11385.2762197...],
                          [   470.        ,  11413.0143813...],
                          [   471.        ,  11440.4477705...],
                          [   472.        ,  11467.5768165...],
                          [   473.        ,  11494.4019726...],
                          [   474.        ,  11520.9237164...],
                          [   475.        ,  11547.1425485...],
                          [   476.        ,  11573.0589928...],
                          [   477.        ,  11598.6735959...],
                          [   478.        ,  11623.9869264...],
                          [   479.        ,  11648.9995750...],
                          [   480.        ,  11673.7121534...],
                          [   481.        ,  11698.1252948...],
                          [   482.        ,  11722.2396526...],
                          [   483.        ,  11746.0559008...],
                          [   484.        ,  11769.5747329...],
                          [   485.        ,  11792.7968621...],
                          [   486.        ,  11815.7230205...],
                          [   487.        ,  11838.3539591...],
                          [   488.        ,  11860.6904469...],
                          [   489.        ,  11882.7332712...],
                          [   490.        ,  11904.4832366...],
                          [   491.        ,  11925.9411650...],
                          [   492.        ,  11947.1078953...],
                          [   493.        ,  11967.9842826...],
                          [   494.        ,  11988.5711984...],
                          [   495.        ,  12008.8695298...],
                          [   496.        ,  12028.8801795...],
                          [   497.        ,  12048.6040651...],
                          [   498.        ,  12068.0421192...],
                          [   499.        ,  12087.1952887...],
                          [   500.        ,  12106.0645344...],
                          [   501.        ,  12124.6508312...],
                          [   502.        ,  12142.9551672...],
                          [   503.        ,  12160.9785437...],
                          [   504.        ,  12178.7219748...],
                          [   505.        ,  12196.1864870...],
                          [   506.        ,  12213.3731190...],
                          [   507.        ,  12230.2829214...],
                          [   508.        ,  12246.9169563...],
                          [   509.        ,  12263.2762971...],
                          [   510.        ,  12279.3620282...],
                          [   511.        ,  12295.1752445...],
                          [   512.        ,  12310.7170514...],
                          [   513.        ,  12325.9885643...],
                          [   514.        ,  12340.9909086...],
                          [   515.        ,  12355.7252189...],
                          [   516.        ,  12370.1926394...],
                          [   517.        ,  12384.3943230...],
                          [   518.        ,  12398.3314315...],
                          [   519.        ,  12412.0051350...],
                          [   520.        ,  12425.4166118...],
                          [   521.        ,  12438.5670483...],
                          [   522.        ,  12451.4576382...],
                          [   523.        ,  12464.0895830...],
                          [   524.        ,  12476.4640911...],
                          [   525.        ,  12488.5823780...],
                          [   526.        ,  12500.4456657...],
                          [   527.        ,  12512.0551828...],
                          [   528.        ,  12523.4121640...],
                          [   529.        ,  12534.5178499...],
                          [   530.        ,  12545.3734871...],
                          [   531.        ,  12555.9803275...],
                          [   532.        ,  12566.3396282...],
                          [   533.        ,  12576.4526517...],
                          [   534.        ,  12586.3206651...],
                          [   535.        ,  12595.9449403...],
                          [   536.        ,  12605.3267534...],
                          [   537.        ,  12614.4673849...],
                          [   538.        ,  12623.3681194...],
                          [   539.        ,  12632.0302452...],
                          [   540.        ,  12640.4550541...],
                          [   541.        ,  12648.6438417...],
                          [   542.        ,  12656.5979064...],
                          [   543.        ,  12664.3185499...],
                          [   544.        ,  12671.8070768...],
                          [   545.        ,  12679.0647943...],
                          [   546.        ,  12686.0930120...],
                          [   547.        ,  12692.8930419...],
                          [   548.        ,  12699.4661982...],
                          [   549.        ,  12705.8137971...],
                          [   550.        ,  12711.9371564...],
                          [   551.        ,  12717.8375957...],
                          [   552.        ,  12723.5164362...],
                          [   553.        ,  12728.9750001...],
                          [   554.        ,  12734.2146109...],
                          [   555.        ,  12739.2365933...],
                          [   556.        ,  12744.0422724...],
                          [   557.        ,  12748.6329745...],
                          [   558.        ,  12753.0100260...],
                          [   559.        ,  12757.1747541...],
                          [   560.        ,  12761.1284859...],
                          [   561.        ,  12764.8725489...],
                          [   562.        ,  12768.4082704...],
                          [   563.        ,  12771.7369777...],
                          [   564.        ,  12774.8599976...],
                          [   565.        ,  12777.7786567...],
                          [   566.        ,  12780.4942809...],
                          [   567.        ,  12783.0081955...],
                          [   568.        ,  12785.3217250...],
                          [   569.        ,  12787.4361930...],
                          [   570.        ,  12789.3529220...],
                          [   571.        ,  12791.0732335...],
                          [   572.        ,  12792.5984474...],
                          [   573.        ,  12793.9298826...],
                          [   574.        ,  12795.0688562...],
                          [   575.        ,  12796.0166840...],
                          [   576.        ,  12796.7746799...],
                          [   577.        ,  12797.3441559...],
                          [   578.        ,  12797.7264224...],
                          [   579.        ,  12797.9227874...],
                          [   580.        ,  12797.9345572...],
                          [   581.        ,  12797.7630356...],
                          [   582.        ,  12797.4095241...],
                          [   583.        ,  12796.8753220...],
                          [   584.        ,  12796.1617260...],
                          [   585.        ,  12795.2700302...],
                          [   586.        ,  12794.2015261...],
                          [   587.        ,  12792.9575025...],
                          [   588.        ,  12791.5392453...],
                          [   589.        ,  12789.9480374...],
                          [   590.        ,  12788.1851590...],
                          [   591.        ,  12786.2518870...],
                          [   592.        ,  12784.1494952...],
                          [   593.        ,  12781.8792543...],
                          [   594.        ,  12779.4424316...],
                          [   595.        ,  12776.8402910...],
                          [   596.        ,  12774.0740932...],
                          [   597.        ,  12771.1450952...],
                          [   598.        ,  12768.0545506...],
                          [   599.        ,  12764.8037091...],
                          [   600.        ,  12761.3938171...],
                          [   601.        ,  12757.8261171...],
                          [   602.        ,  12754.1018476...],
                          [   603.        ,  12750.2222435...],
                          [   604.        ,  12746.1885357...],
                          [   605.        ,  12742.0019511...],
                          [   606.        ,  12737.6637126...],
                          [   607.        ,  12733.1750389...],
                          [   608.        ,  12728.5371449...],
                          [   609.        ,  12723.7512409...],
                          [   610.        ,  12718.8185333...],
                          [   611.        ,  12713.7402241...],
                          [   612.        ,  12708.5175109...],
                          [   613.        ,  12703.1515870...],
                          [   614.        ,  12697.6436414...],
                          [   615.        ,  12691.9948585...],
                          [   616.        ,  12686.2064183...],
                          [   617.        ,  12680.2794963...],
                          [   618.        ,  12674.2152632...],
                          [   619.        ,  12668.0148855...],
                          [   620.        ,  12661.6795247...],
                          [   621.        ,  12655.2103378...],
                          [   622.        ,  12648.6084770...],
                          [   623.        ,  12641.8750899...],
                          [   624.        ,  12635.0113192...],
                          [   625.        ,  12628.0183029...],
                          [   626.        ,  12620.8971740...],
                          [   627.        ,  12613.6490609...],
                          [   628.        ,  12606.2750869...],
                          [   629.        ,  12598.7763704...],
                          [   630.        ,  12591.1540251...],
                          [   631.        ,  12583.4091595...],
                          [   632.        ,  12575.5428771...],
                          [   633.        ,  12567.5562766...],
                          [   634.        ,  12559.4504515...],
                          [   635.        ,  12551.2264904...],
                          [   636.        ,  12542.8854766...],
                          [   637.        ,  12534.4284886...],
                          [   638.        ,  12525.8565997...],
                          [   639.        ,  12517.1708779...],
                          [   640.        ,  12508.3723863...],
                          [   641.        ,  12499.4621828...],
                          [   642.        ,  12490.4413201...],
                          [   643.        ,  12481.3108457...],
                          [   644.        ,  12472.0718019...],
                          [   645.        ,  12462.7252260...],
                          [   646.        ,  12453.2721498...],
                          [   647.        ,  12443.7136000...],
                          [   648.        ,  12434.0505982...],
                          [   649.        ,  12424.2841606...],
                          [   650.        ,  12414.4152982...],
                          [   651.        ,  12404.4450167...],
                          [   652.        ,  12394.3743166...],
                          [   653.        ,  12384.2041931...],
                          [   654.        ,  12373.9356362...],
                          [   655.        ,  12363.5696306...],
                          [   656.        ,  12353.1071555...],
                          [   657.        ,  12342.5491851...],
                          [   658.        ,  12331.8966883...],
                          [   659.        ,  12321.1506285...],
                          [   660.        ,  12310.3119640...],
                          [   661.        ,  12299.3816476...],
                          [   662.        ,  12288.3606272...],
                          [   663.        ,  12277.2498448...],
                          [   664.        ,  12266.0502378...],
                          [   665.        ,  12254.7627377...],
                          [   666.        ,  12243.3882711...],
                          [   667.        ,  12231.9277592...],
                          [   668.        ,  12220.3821179...],
                          [   669.        ,  12208.7522577...],
                          [   670.        ,  12197.0390841...],
                          [   671.        ,  12185.2434970...],
                          [   672.        ,  12173.3663914...],
                          [   673.        ,  12161.4086567...],
                          [   674.        ,  12149.3711771...],
                          [   675.        ,  12137.2548318...],
                          [   676.        ,  12125.0604945...],
                          [   677.        ,  12112.7890338...],
                          [   678.        ,  12100.4413128...],
                          [   679.        ,  12088.0181898...],
                          [   680.        ,  12075.5205176...],
                          [   681.        ,  12062.9491438...],
                          [   682.        ,  12050.3049109...],
                          [   683.        ,  12037.5886562...],
                          [   684.        ,  12024.8012117...],
                          [   685.        ,  12011.9434044...],
                          [   686.        ,  11999.016056 ...],
                          [   687.        ,  11986.0199830...],
                          [   688.        ,  11972.9559971...],
                          [   689.        ,  11959.8249045...],
                          [   690.        ,  11946.6275064...],
                          [   691.        ,  11933.3645990...],
                          [   692.        ,  11920.0369733...],
                          [   693.        ,  11906.6454152...],
                          [   694.        ,  11893.1907055...],
                          [   695.        ,  11879.6736202...],
                          [   696.        ,  11866.0949300...],
                          [   697.        ,  11852.4554007...],
                          [   698.        ,  11838.7557929...],
                          [   699.        ,  11824.9968625...],
                          [   700.        ,  11811.1793602...],
                          [   701.        ,  11797.3040317...],
                          [   702.        ,  11783.3716180...],
                          [   703.        ,  11769.3828548...],
                          [   704.        ,  11755.3384733...],
                          [   705.        ,  11741.2391993...],
                          [   706.        ,  11727.0857541...],
                          [   707.        ,  11712.878854 ...],
                          [   708.        ,  11698.6192103...],
                          [   709.        ,  11684.3075296...],
                          [   710.        ,  11669.9445138...],
                          [   711.        ,  11655.5308596...],
                          [   712.        ,  11641.0672593...],
                          [   713.        ,  11626.5544002...],
                          [   714.        ,  11611.9929648...],
                          [   715.        ,  11597.3836310...],
                          [   716.        ,  11582.7270720...],
                          [   717.        ,  11568.0239562...],
                          [   718.        ,  11553.2749471...],
                          [   719.        ,  11538.4807040...],
                          [   720.        ,  11523.6418811...],
                          [   721.        ,  11508.7591283...],
                          [   722.        ,  11493.8330905...],
                          [   723.        ,  11478.8644085...],
                          [   724.        ,  11463.8537180...],
                          [   725.        ,  11448.8016505...],
                          [   726.        ,  11433.7088327...],
                          [   727.        ,  11418.5758871...],
                          [   728.        ,  11403.4034314...],
                          [   729.        ,  11388.1920788...],
                          [   730.        ,  11372.9424382...],
                          [   731.        ,  11357.6551141...],
                          [   732.        ,  11342.3307063...],
                          [   733.        ,  11326.9698104...],
                          [   734.        ,  11311.5730175...],
                          [   735.        ,  11296.1409144...],
                          [   736.        ,  11280.6740836...],
                          [   737.        ,  11265.1731031...],
                          [   738.        ,  11249.6385466...],
                          [   739.        ,  11234.0709837...],
                          [   740.        ,  11218.4709796...],
                          [   741.        ,  11202.8390952...],
                          [   742.        ,  11187.1758873...],
                          [   743.        ,  11171.4819083...],
                          [   744.        ,  11155.7577065...],
                          [   745.        ,  11140.0038261...],
                          [   746.        ,  11124.2208070...],
                          [   747.        ,  11108.4091852...],
                          [   748.        ,  11092.5694922...],
                          [   749.        ,  11076.7022559...],
                          [   750.        ,  11060.8079996...],
                          [   751.        ,  11044.8872430...],
                          [   752.        ,  11028.9405016...],
                          [   753.        ,  11012.9682867...],
                          [   754.        ,  10996.9711059...],
                          [   755.        ,  10980.9494627...],
                          [   756.        ,  10964.9038566...],
                          [   757.        ,  10948.8347833...],
                          [   758.        ,  10932.7427345...],
                          [   759.        ,  10916.6281979...],
                          [   760.        ,  10900.4916576...],
                          [   761.        ,  10884.3335937...],
                          [   762.        ,  10868.1544824...],
                          [   763.        ,  10851.9547962...],
                          [   764.        ,  10835.7350038...],
                          [   765.        ,  10819.4955701...],
                          [   766.        ,  10803.2369563...],
                          [   767.        ,  10786.9596199...],
                          [   768.        ,  10770.6640145...],
                          [   769.        ,  10754.3505902...],
                          [   770.        ,  10738.0197934...],
                          [   771.        ,  10721.6720668...],
                          [   772.        ,  10705.3078497...],
                          [   773.        ,  10688.9275774...],
                          [   774.        ,  10672.5316819...],
                          [   775.        ,  10656.1205916...],
                          [   776.        ,  10639.6947313...],
                          [   777.        ,  10623.2545223...],
                          [   778.        ,  10606.8003824...],
                          [   779.        ,  10590.3327259...],
                          [   780.        ,  10573.8519636...]],
                         interpolator=SpragueInterpolator,
                         interpolator_kwargs={},
                         extrapolator=Extrapolator,
                         extrapolator_kwargs={...})
    """

    wavelengths = shape.range()
    return SpectralDistribution(
        planck_law(wavelengths * 1e-9, temperature, c1, c2, n) * 1e-9,
        wavelengths,
        name=f"{temperature}K Blackbody",
    )
