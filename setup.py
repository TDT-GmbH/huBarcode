long_description = """
huBarcode contains a collection of tools to generate various 1D and 2D barcvodes in Python.
"""

from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

# patch distutils if it can't cope with the "classifiers" or
# "download_url" keywords
from sys import version
if version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None
            
hubarcode = setup(name='huBarcode',
    maintainer='Maximillian Dornseif',
    maintainer_email='md@hudora.de',
    url='http://github.com/hudora/huBarcode',
    version='0.56p4',
    description='generation of barcodes in Python',
    long_description=long_description,
    classifiers=['License :: OSI Approved :: BSD License',
                 'Intended Audience :: Developers',
                 'Programming Language :: Python',
                 'Topic :: Multimedia :: Graphics',
                 'Topic :: Office/Business'],
    # download_url
    package_dir = {'huBarcode': ''},
    packages=['huBarcode', 'huBarcode.qrcode', 'huBarcode.qrcode.qrcode_data',
              'huBarcode.datamatrix', 'huBarcode.ean13', 'huBarcode.code128'],
    data_files=[('fonts', ['fonts/cour.pbm', 'fonts/cour.pil', 'fonts/courR08.pbm', 'fonts/courR08.pil',
                           'fonts/courR10.pbm', 'fonts/courR10.pil', 'fonts/courR12.pbm',
                           'fonts/courR12.pil', 'fonts/courR14.pbm', 'fonts/courR14.pil',
                           'fonts/courR18.pbm', 'fonts/courR18.pil', 'fonts/courR24.pbm',
                           'fonts/courR24.pil']),
                ('huBarcode/qrcode/qrcode_data', [ 'qrcode/qrcode_data/qrv10_0.dat',
                           'qrcode/qrcode_data/qrv10_1.dat', 'qrcode/qrcode_data/qrv10_2.dat',
                           'qrcode/qrcode_data/qrv10_3.dat', 'qrcode/qrcode_data/qrv11_0.dat',
                           'qrcode/qrcode_data/qrv11_1.dat', 'qrcode/qrcode_data/qrv11_2.dat',
                           'qrcode/qrcode_data/qrv11_3.dat', 'qrcode/qrcode_data/qrv12_0.dat',
                           'qrcode/qrcode_data/qrv12_1.dat', 'qrcode/qrcode_data/qrv12_2.dat',
                           'qrcode/qrcode_data/qrv12_3.dat', 'qrcode/qrcode_data/qrv13_0.dat',
                           'qrcode/qrcode_data/qrv13_1.dat', 'qrcode/qrcode_data/qrv13_2.dat',
                           'qrcode/qrcode_data/qrv13_3.dat', 'qrcode/qrcode_data/qrv14_0.dat',
                           'qrcode/qrcode_data/qrv14_1.dat', 'qrcode/qrcode_data/qrv14_2.dat',
                           'qrcode/qrcode_data/qrv14_3.dat', 'qrcode/qrcode_data/qrv15_0.dat',
                           'qrcode/qrcode_data/qrv15_1.dat', 'qrcode/qrcode_data/qrv15_2.dat',
                           'qrcode/qrcode_data/qrv15_3.dat', 'qrcode/qrcode_data/qrv16_0.dat',
                           'qrcode/qrcode_data/qrv16_1.dat', 'qrcode/qrcode_data/qrv16_2.dat',
                           'qrcode/qrcode_data/qrv16_3.dat', 'qrcode/qrcode_data/qrv17_0.dat',
                           'qrcode/qrcode_data/qrv17_1.dat', 'qrcode/qrcode_data/qrv17_2.dat',
                           'qrcode/qrcode_data/qrv17_3.dat', 'qrcode/qrcode_data/qrv18_0.dat',
                           'qrcode/qrcode_data/qrv18_1.dat', 'qrcode/qrcode_data/qrv18_2.dat',
                           'qrcode/qrcode_data/qrv18_3.dat', 'qrcode/qrcode_data/qrv19_0.dat',
                           'qrcode/qrcode_data/qrv19_1.dat', 'qrcode/qrcode_data/qrv19_2.dat',
                           'qrcode/qrcode_data/qrv19_3.dat', 'qrcode/qrcode_data/qrv1_0.dat' ,
                           'qrcode/qrcode_data/qrv1_1.dat' , 'qrcode/qrcode_data/qrv1_2.dat' ,
                           'qrcode/qrcode_data/qrv1_3.dat' , 'qrcode/qrcode_data/qrv20_0.dat',
                           'qrcode/qrcode_data/qrv20_1.dat', 'qrcode/qrcode_data/qrv20_2.dat',
                           'qrcode/qrcode_data/qrv20_3.dat', 'qrcode/qrcode_data/qrv21_0.dat',
                           'qrcode/qrcode_data/qrv21_1.dat', 'qrcode/qrcode_data/qrv21_2.dat',
                           'qrcode/qrcode_data/qrv21_3.dat', 'qrcode/qrcode_data/qrv22_0.dat',
                           'qrcode/qrcode_data/qrv22_1.dat', 'qrcode/qrcode_data/qrv22_2.dat',
                           'qrcode/qrcode_data/qrv22_3.dat', 'qrcode/qrcode_data/qrv23_0.dat',
                           'qrcode/qrcode_data/qrv23_1.dat', 'qrcode/qrcode_data/qrv23_2.dat',
                           'qrcode/qrcode_data/qrv23_3.dat', 'qrcode/qrcode_data/qrv24_0.dat',
                           'qrcode/qrcode_data/qrv24_1.dat', 'qrcode/qrcode_data/qrv24_2.dat',
                           'qrcode/qrcode_data/qrv24_3.dat', 'qrcode/qrcode_data/qrv25_0.dat',
                           'qrcode/qrcode_data/qrv25_1.dat', 'qrcode/qrcode_data/qrv25_2.dat',
                           'qrcode/qrcode_data/qrv25_3.dat', 'qrcode/qrcode_data/qrv26_0.dat',
                           'qrcode/qrcode_data/qrv26_1.dat', 'qrcode/qrcode_data/qrv26_2.dat',
                           'qrcode/qrcode_data/qrv26_3.dat', 'qrcode/qrcode_data/qrv27_0.dat',
                           'qrcode/qrcode_data/qrv27_1.dat', 'qrcode/qrcode_data/qrv27_2.dat',
                           'qrcode/qrcode_data/qrv27_3.dat', 'qrcode/qrcode_data/qrv28_0.dat',
                           'qrcode/qrcode_data/qrv28_1.dat', 'qrcode/qrcode_data/qrv28_2.dat',
                           'qrcode/qrcode_data/qrv28_3.dat', 'qrcode/qrcode_data/qrv29_0.dat',
                           'qrcode/qrcode_data/qrv29_1.dat', 'qrcode/qrcode_data/qrv29_2.dat',
                           'qrcode/qrcode_data/qrv29_3.dat', 'qrcode/qrcode_data/qrv2_0.dat' ,
                           'qrcode/qrcode_data/qrv2_1.dat' , 'qrcode/qrcode_data/qrv2_2.dat' ,
                           'qrcode/qrcode_data/qrv2_3.dat' , 'qrcode/qrcode_data/qrv30_0.dat',
                           'qrcode/qrcode_data/qrv30_1.dat', 'qrcode/qrcode_data/qrv30_2.dat',
                           'qrcode/qrcode_data/qrv30_3.dat', 'qrcode/qrcode_data/qrv31_0.dat',
                           'qrcode/qrcode_data/qrv31_1.dat', 'qrcode/qrcode_data/qrv31_2.dat',
                           'qrcode/qrcode_data/qrv31_3.dat', 'qrcode/qrcode_data/qrv32_0.dat',
                           'qrcode/qrcode_data/qrv32_1.dat', 'qrcode/qrcode_data/qrv32_2.dat',
                           'qrcode/qrcode_data/qrv32_3.dat', 'qrcode/qrcode_data/qrv33_0.dat',
                           'qrcode/qrcode_data/qrv33_1.dat', 'qrcode/qrcode_data/qrv33_2.dat',
                           'qrcode/qrcode_data/qrv33_3.dat', 'qrcode/qrcode_data/qrv34_0.dat',
                           'qrcode/qrcode_data/qrv34_1.dat', 'qrcode/qrcode_data/qrv34_2.dat',
                           'qrcode/qrcode_data/qrv34_3.dat', 'qrcode/qrcode_data/qrv35_0.dat',
                           'qrcode/qrcode_data/qrv35_1.dat', 'qrcode/qrcode_data/qrv35_2.dat',
                           'qrcode/qrcode_data/qrv35_3.dat', 'qrcode/qrcode_data/qrv36_0.dat',
                           'qrcode/qrcode_data/qrv36_1.dat', 'qrcode/qrcode_data/qrv36_2.dat',
                           'qrcode/qrcode_data/qrv36_3.dat', 'qrcode/qrcode_data/qrv37_0.dat',
                           'qrcode/qrcode_data/qrv37_1.dat', 'qrcode/qrcode_data/qrv37_2.dat',
                           'qrcode/qrcode_data/qrv37_3.dat', 'qrcode/qrcode_data/qrv38_0.dat',
                           'qrcode/qrcode_data/qrv38_1.dat', 'qrcode/qrcode_data/qrv38_2.dat',
                           'qrcode/qrcode_data/qrv38_3.dat', 'qrcode/qrcode_data/qrv39_0.dat',
                           'qrcode/qrcode_data/qrv39_1.dat', 'qrcode/qrcode_data/qrv39_2.dat',
                           'qrcode/qrcode_data/qrv39_3.dat', 'qrcode/qrcode_data/qrv3_0.dat' ,
                           'qrcode/qrcode_data/qrv3_1.dat' , 'qrcode/qrcode_data/qrv3_2.dat' ,
                           'qrcode/qrcode_data/qrv3_3.dat' , 'qrcode/qrcode_data/qrv40_0.dat',
                           'qrcode/qrcode_data/qrv40_1.dat', 'qrcode/qrcode_data/qrv40_2.dat',
                           'qrcode/qrcode_data/qrv40_3.dat', 'qrcode/qrcode_data/qrv4_0.dat' ,
                           'qrcode/qrcode_data/qrv4_1.dat' , 'qrcode/qrcode_data/qrv4_2.dat' ,
                           'qrcode/qrcode_data/qrv4_3.dat' , 'qrcode/qrcode_data/qrv5_0.dat' ,
                           'qrcode/qrcode_data/qrv5_1.dat' , 'qrcode/qrcode_data/qrv5_2.dat' ,
                           'qrcode/qrcode_data/qrv5_3.dat' , 'qrcode/qrcode_data/qrv6_0.dat' ,
                           'qrcode/qrcode_data/qrv6_1.dat' , 'qrcode/qrcode_data/qrv6_2.dat' ,
                           'qrcode/qrcode_data/qrv6_3.dat' , 'qrcode/qrcode_data/qrv7_0.dat' ,
                           'qrcode/qrcode_data/qrv7_1.dat' , 'qrcode/qrcode_data/qrv7_2.dat' ,
                           'qrcode/qrcode_data/qrv7_3.dat' , 'qrcode/qrcode_data/qrv8_0.dat' ,
                           'qrcode/qrcode_data/qrv8_1.dat' , 'qrcode/qrcode_data/qrv8_2.dat' ,
                           'qrcode/qrcode_data/qrv8_3.dat' , 'qrcode/qrcode_data/qrv9_0.dat' ,
                           'qrcode/qrcode_data/qrv9_1.dat' , 'qrcode/qrcode_data/qrv9_2.dat' ,
                           'qrcode/qrcode_data/qrv9_3.dat' , 'qrcode/qrcode_data/qrvfr1.dat' ,
                           'qrcode/qrcode_data/qrvfr10.dat', 'qrcode/qrcode_data/qrvfr11.dat',
                           'qrcode/qrcode_data/qrvfr12.dat', 'qrcode/qrcode_data/qrvfr13.dat',
                           'qrcode/qrcode_data/qrvfr14.dat', 'qrcode/qrcode_data/qrvfr15.dat',
                           'qrcode/qrcode_data/qrvfr16.dat', 'qrcode/qrcode_data/qrvfr17.dat',
                           'qrcode/qrcode_data/qrvfr18.dat', 'qrcode/qrcode_data/qrvfr19.dat',
                           'qrcode/qrcode_data/qrvfr2.dat' , 'qrcode/qrcode_data/qrvfr20.dat',
                           'qrcode/qrcode_data/qrvfr21.dat', 'qrcode/qrcode_data/qrvfr22.dat',
                           'qrcode/qrcode_data/qrvfr23.dat', 'qrcode/qrcode_data/qrvfr24.dat',
                           'qrcode/qrcode_data/qrvfr25.dat', 'qrcode/qrcode_data/qrvfr26.dat',
                           'qrcode/qrcode_data/qrvfr27.dat', 'qrcode/qrcode_data/qrvfr28.dat',
                           'qrcode/qrcode_data/qrvfr29.dat', 'qrcode/qrcode_data/qrvfr3.dat' ,
                           'qrcode/qrcode_data/qrvfr30.dat', 'qrcode/qrcode_data/qrvfr31.dat',
                           'qrcode/qrcode_data/qrvfr32.dat', 'qrcode/qrcode_data/qrvfr33.dat',
                           'qrcode/qrcode_data/qrvfr34.dat', 'qrcode/qrcode_data/qrvfr35.dat',
                           'qrcode/qrcode_data/qrvfr36.dat', 'qrcode/qrcode_data/qrvfr37.dat',
                           'qrcode/qrcode_data/qrvfr38.dat', 'qrcode/qrcode_data/qrvfr39.dat',
                           'qrcode/qrcode_data/qrvfr4.dat' , 'qrcode/qrcode_data/qrvfr40.dat',
                           'qrcode/qrcode_data/qrvfr5.dat' , 'qrcode/qrcode_data/qrvfr6.dat' ,
                           'qrcode/qrcode_data/qrvfr7.dat' , 'qrcode/qrcode_data/qrvfr8.dat' ,
                           'qrcode/qrcode_data/qrvfr9.dat' , 'qrcode/qrcode_data/rsc10.dat' ,
                           'qrcode/qrcode_data/rsc13.dat' , 'qrcode/qrcode_data/rsc15.dat' ,
                           'qrcode/qrcode_data/rsc16.dat' , 'qrcode/qrcode_data/rsc17.dat' ,
                           'qrcode/qrcode_data/rsc18.dat' , 'qrcode/qrcode_data/rsc20.dat' ,
                           'qrcode/qrcode_data/rsc22.dat' , 'qrcode/qrcode_data/rsc24.dat' ,
                           'qrcode/qrcode_data/rsc26.dat' , 'qrcode/qrcode_data/rsc28.dat' ,
                           'qrcode/qrcode_data/rsc30.dat' , 'qrcode/qrcode_data/rsc32.dat' ,
                           'qrcode/qrcode_data/rsc34.dat' , 'qrcode/qrcode_data/rsc36.dat' ,
                           'qrcode/qrcode_data/rsc40.dat' , 'qrcode/qrcode_data/rsc42.dat' ,
                           'qrcode/qrcode_data/rsc44.dat' , 'qrcode/qrcode_data/rsc46.dat' ,
                           'qrcode/qrcode_data/rsc48.dat' , 'qrcode/qrcode_data/rsc50.dat' ,
                           'qrcode/qrcode_data/rsc52.dat' , 'qrcode/qrcode_data/rsc54.dat' ,
                           'qrcode/qrcode_data/rsc56.dat' , 'qrcode/qrcode_data/rsc58.dat' ,
                           'qrcode/qrcode_data/rsc60.dat' , 'qrcode/qrcode_data/rsc62.dat' ,
                           'qrcode/qrcode_data/rsc64.dat' , 'qrcode/qrcode_data/rsc66.dat' ,
                           'qrcode/qrcode_data/rsc68.dat' , 'qrcode/qrcode_data/rsc7.dat' , ])],
    zip_safe=False,
)
