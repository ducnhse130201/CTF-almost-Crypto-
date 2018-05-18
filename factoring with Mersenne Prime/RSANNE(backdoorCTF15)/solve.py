from libnum import *
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
n = 658416274830184544125027519921443515789888264156074733099244040126213682497714032798116399288176502462829255784525977722903018714434309698108208388664768262754316426220651576623731617882923164117579624827261244506084274371250277849351631679441171018418018498039996472549893150577189302871520311715179730714312181456245097848491669795997289830612988058523968384808822828370900198489249243399165125219244753790779764466236965135793576516193213175061401667388622228362042717054014679032953441034021506856017081062617572351195418505899388715709795992029559042119783423597324707100694064675909238717573058764118893225111602703838080618565401139902143069901117174204252871948846864436771808616432457102844534843857198735242005309073939051433790946726672234643259349535186268571629077937597838801337973092285608744209951533199868228040004432132597073390363357892379997655878857696334892216345070227646749851381208554044940444182864026513709449823489593439017366358869648168238735087593808344484365136284219725233811605331815007424582890821887260682886632543613109252862114326372077785369292570900594814481097443781269562647303671428895764224084402259605109600363098950091998891375812839523613295667253813978434879172781217285652895469194181218343078754501694746598738215243769747956572555989594598180639098344891175879455994652382137038240166358066403475457
e = long(65537)
#factoring N by Mersenne Prime (2^k - 1)
a = 4
while True:
	if a > n:
		break
	if n % (a - 1) == 0:
		print 'Found!!'
		p = n / (a-1)
		q = a-1
		print p,q
    		break
  	a = a * 2
#decrypting (be careful with OAEP)
phi = (p-1)*(q-1)
d = modular.invmod(e,phi)
key = PKCS1_OAEP.new(RSA.construct((n,e,d)))
with open('flag.enc','r') as f:
	c = base64.b64decode(f.read())
print s2n(c)
m = key.decrypt(c)
print m

