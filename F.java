/*
c'est un algorithme de surface
la surface totale = somme des petites surfaces
et donc on calcule la surface totale et on divise / largeur
*/
public class F {

	public static void main(String[] args) {
		int N=7;
		int w=4;
		int wi[]= {2,1,1,1,1,2,2,2};
		int hi[]= {3,4,2,2,2,2,2,1};
		int surf=0;
		while(N>0) {
			surf=surf+(wi[N-1]*hi[N-1]);
			N--;
		}
		System.out.println("l="+surf/w);
	}

}
