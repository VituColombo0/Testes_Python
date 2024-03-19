m = float(input('Digite um valor em metros: '))

km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print('O valor em Quilômetro {} \n Hectômetro {} \n Decâmetro {} \n Metro {} \n Decímetro {} \n Centímetro {} \n Milímetro {}'.format(
    km, hm, dam, m, dm, cm, mm))
