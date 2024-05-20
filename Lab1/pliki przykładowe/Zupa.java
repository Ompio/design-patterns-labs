package pl.kurs.restauracja;

import java.util.ArrayList;
import java.util.List;

public class Zupa {
	List<Skladnik> skladniki = new ArrayList<Skladnik>();
	
	String nazwa;
	
	public void przygotuj() {
		System.out.println("Przygotowanie zupy ze sk³adników: "+skladniki);
		System.out.println("Nalewam wodê do garnka");
		System.out.println("Wrzucam kostkê roso³ow¹");
		nazwa = "rosó³";
		for(Skladnik skladnik:skladniki) {
			if(skladnik instanceof Marchewka) {
				Marchewka marchewka = (Marchewka)skladnik;
				marchewka.obierz();
				marchewka.pokroj();
			}
			if(skladnik instanceof Makaron) {
				Makaron makaron = (Makaron)skladnik;
				makaron.gotuj();
			}
			
		}
			
	}
	
	public void podaj() {
		System.out.println("Podanie obiadu");
		System.out.println("Podajê "+nazwa+ " do sto³u");
	}
	
}
