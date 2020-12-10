import java.util.Scanner;
import static java.lang.System.out;

public class A {
	
	
	//l'idée est de faire la soustraction
	//entre les deux ensembles out et in, la valeur qui
	//est la plus répétée est élue comme temps de cuisson
	public static void main(String[] args) {
		Scanner read = new Scanner(System.in);
		out.println("Give N: ");
	    int N = read.nextInt();
	    out.println("Give M: ");
	    int M = read.nextInt();
		int in[]= new int[N];
		int exit[]= new int[M];
		
		out.print("Give in times: \n");
	    for (int i = 0; i < N; i++) {
			out.print("--->");
	    	in[i]=read.nextInt();
		}
	    out.print("Give out times: \n");
	    for (int i = 0; i < M; i++) {
			out.print("--->");
	    	exit[i]=read.nextInt();
		}


		int minus[]=new int[N*M];int index=0;
		int i=0,j;
		while(i<M) {
			j=0;
			while(j<N && exit[i]>in[j]) {//optimiser la boucle, inutile de continuer si out<in
				minus[index]=exit[i]-in[j];
				index++;
				j++;
			}
			i++;
		}

		System.out.print("Duration is: "+getMostFrequentElement(minus,index));
		
	}
	
	
	//cette fonction retourne l'element le plus frequent 
	public static int getMostFrequentElement(int tab[], int size) {
		int count = 1, tempCount;
		  int popular = tab[0];
		  int temp = 0;
		  for (int i = 0; i < (size - 1); i++)
		  {
		    temp = tab[i];
		    tempCount = 0;
		    for (int j = 1; j < size; j++)
		    {
		      if (temp == tab[j])
		        tempCount++;
		    }
		    if (tempCount > count)
		    {
		      popular = temp;
		      count = tempCount;
		    }
		  }
		  return popular;
	}

}
