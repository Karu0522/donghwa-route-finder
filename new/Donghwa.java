import java.util.*;
public class Donghwa {

	static int[][] graph = {
			{},
		    {2,3,5,6}, //1. Central
		    {1,3,11}, //2. Seaside
		    {1,2,4,5,10,11}, //3. Newmoon
		    {3,5,7,8,9,10}, //4. Neo
		    {1,3,4,6,7}, //5. Day
		    {1,5,7,19,20}, //6. Nova
		    {4,5,6,8,19}, //7. Dream
		    {4,7,9,17,18,19}, //8. Lato
		    {4,8,10,15,16,17}, //9. Snow
		    {3,4,9,11,13,14,15}, //10. Wind
		    {2,3,10,12,13}, //11. Raon
		    {11,13}, //12. Nitro
		    {10,11,12,14}, //13. Starfield
		    {10,13,15}, //14. Sky
		    {9,10,14,16}, //15. Haru
		    {9,15,17}, //16. Bluetree
		    {8,9,16,18}, //17. Pearland
		    {8,17,19}, //18. Miso
		    {6,7,8,18,20}, //19. Truetown
		    {6,19} //20. Mancho
		};
		
	static String[] name = {
		"",
		"Central",
		"Seaside",
		"Newmoon",
		"Neo",
		"Day",
		"Nova",
		"Dream",
		"Lato",
		"Snow",
		"Wind",
		"Raon",
		"Nitro",
		"Starfield",
		"Sky",
		"Haru",
		"Bluetree",
		"Pearland",
		"Miso",
		"Truetown",
		"Mancho"
	};

    static int[] visited = new int[21];
    static int[] distance = new int[21];
    static ArrayDeque<Integer> queue = new ArrayDeque<>();
    
    public static int[] init(int[] a)
    {
        for(int i=0;i<a.length;i++)
            a[i] = 0;
        return a;
    }
    
    public static void search(int start, int end)
    {
        init(visited);
        init(distance);
        visited[start] = 1;
        queue.add(start);
        while(!queue.isEmpty())
        {
            int v = queue.poll();
            // System.out.printf("%d ",v);
            for(int n : graph[v])
            {
                if(visited[n]==0)
                {
                    distance[n]=distance[v]+1;
                    visited[n]=1;
                    queue.add(n); 
                }
            }
        }
        System.out.printf("%s에서 %s까지의 거리: %d\n",name[start],name[end],distance[end]);
    }
    
    public static int find(String a)
    {
    	int n=0;
    	for(int i=1;i<name.length;i++)
        {
            if(a.equals(name[i]))
            {
                n=i;
            }
        }
    	return n;
    }
    
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int start=0;
        int end=0;
        String s1, s2;
        while(true)
        {
            
            System.out.print("출발 도시를 입력하세요: ");
            s1=sc.next();
            System.out.print("도착 도시를 입력하세요: ");
            s2=sc.next();
            
            if(s1.equals("q") || s2.equals("q"))
                break;
            start = find(s1);
            end = find(s2);
            if(start != 0 && end != 0)
            {
                if(start==end)
                    System.out.print("출발 도시와 도착 도시가 같습니다. 정신 차리세요.\n");
                else
                    search(start,end);
            }
            else
            {
                System.out.print("존재하지 않는 도시입니다.\n");
            }
        }
    }
}
