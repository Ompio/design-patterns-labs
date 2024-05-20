package pl.kurs.restauracja;

public class Test {
public static void main(String[] args) {
	przygotujZupe();
}
public static void przygotujZupe() {	
	Zupa zupa = new Zupa();
	Marchewka marchewka = new Marchewka();
	zupa.skladniki.add(marchewka);
	Makaron makaron = new Makaron();
	zupa.skladniki.add(makaron);
	zupa.przygotuj();
	zupa.podaj();
}
}
