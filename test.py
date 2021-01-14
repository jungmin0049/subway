import pygame

#def
max_vartices=100
inf=1000000
INT_MAX=inf

change=[["대저",[5,13],[3,0]],["덕천",[3,4],[2,9]],["사상",[2,15],[5,19]],["미남",[3,9],[4,0]],["동래",[4,1],[1,23]],["연산",[3,13],[1,22]],["서면",[2,23],[1,18]],["수영",[3,17],[2,34]]];
t1=["신평","하단","당리","사하","괴정",",대티","서대신","동대신","토성","자갈치","남포","중앙","부산역","초량","부산진","좌천","범일","범내골","서면","부전","양정","시청","연산","동래","명륜","온천장","부산대","장전","구서","두실","남산","범어사","노포"];
t2=["양산","남양","부산대양산캠퍼스","호포","금곡","동원","율리","화명","수정","덕천","구명","구남","모라","모덕","덕포","사상","감전","주례","냉정","개금","동의대","가야","부암","서면","전포","국제금융센터","문현","지개골","못골","대연","경성대","남천","금련산","광안","수영","민락","센텀시티","시립미술관","동백","해운대","중동","장산"];
t3=["대저","체육공원","강서구청","구포","덕천","숙동","남산","남산정","만덕","미남","사직","종합운동장","거제","연산","물만골","배산","망미","수영"];
t4=["미남","동래","수안","낙민","충렬","명장","서동","금사","반여농산물시장","석대","영산대","동부산대학","고촌","안평"];
t5=["가야대","장신대","연지공원","박물관","수로왕릉","봉황","부원","인제대","김해대학","지내","불암","대사","평강","대저","동구","덕두","공항","서부산유통지구","괘법르네시떼","사상"];

def select_T(n):
    if (n==1):
        return t1;
    if (n==2):
        return t2;
    if (n==3):
        return t3;
    if (n==4):
        return t4;
    if (n==5):
        return t5;
    
n=8;
weight=[[0,4,6,inf,inf,inf,inf,inf],[4,0,6,4,inf,inf,inf,inf],[6,6,0,inf,inf,inf,8,inf],[inf,4,inf,0,1,4,inf,inf],[inf,inf,inf,1,0,2,inf,inf],[inf,inf,inf,4,2,0,4,4 ],[inf,inf,8,inf,inf,4,0,11],[inf,inf,inf,inf,inf,4,11,0]]
step=0;

distance=[0]*max_vartices
found=[0]*max_vartices
path=[0]*max_vartices
#for i in change:
#    print(i[0]+" : ")
#    a=select_T(i[1][0])
#    print(a[i[1][1]]);
#    a=select_T(i[2][0])
#    print(a[i[2][1]]);

def choose(distance,found):	
    min = INT_MAX;
    minpos = -1;
    for i in range(n):
	    if ((distance[i] < min) and (0==found[i])):
	    	min = distance[i];
	    	minpos = i;
    return minpos;

def print_status(step):
        
    print("STEP "+str(step)+":" );
    print("distance : ");
    for i in range(n):
	    if (distance[i] == inf):
	    	print(" * ", end="");
	    else:
	    	print(str(distance[i])+" ", end="");
	
    print();
    print(" found : ");
    for i in range(n):
    	print(str(found[i])+" ", end="");
    print("\n");
    step=step+1

def shortest_path(start) :
    step=1
    for i in range(n):
	    distance[i] = weight[start][i];
	    found[i] = False;
	    path[i] = i;
	
    found[start] = True;
    distance[start] = 0;
    for i in range(n-1):
	    print_status(step);
	    step=1+step
	    u = choose(distance, found);
	    found[u] = True;
	    for w in range(n): 
		    if (found[w]==0):
			    if (distance[u] + weight[u][w] < distance[w]) :
				    path[w] = int(path[u]) *10 + w ;
				    distance[w] = distance[u] + weight[u][w];

def closest_change(line,station):
    distance=inf
    for k in range(len(change)):
        i=change[k];
        if(line==i[1][0]):
            if(abs(station-i[1][1])<distance):
                index=k
                distance=abs(station-i[1][1])
        if(line==i[2][0]):
            if(abs(station-i[2][1])<distance):
                index=k
                distance=abs(station-i[2][1])

    return index, distance;
                
            



#shortest_path(5)
##for i in range(n):
##    print(str(path[i])+" ")


line_s=int(input("출발점은 몇호선? : "))
while(1):
    start=input("출발점 : " )
    if start in select_T(line_s):
        s_index=select_T(line_s).index(start)
        break


line_e=int(input("도착점은 몇호선? : "))
while(1):
    end=input("도착점 : " )
    if end in select_T(line_e):
        e_index=select_T(line_e).index(end)
        break

print("출발점 : " + select_T(line_s)[s_index]+"  도착점 : "+select_T(line_e)[e_index])

if (line_s==line_e):
    print(str(line_e)+"호선을 타고 "+str(abs(s_index-e_index))+"정거장을 가시면 됩니다.")
else :
    s_ch,s_dis=closest_change(line_s,s_index)
    e_ch,e_dis=closest_change(line_e,e_index)
    
    print("출발역에서 가장 가까운 환승역 : "+ change[s_ch][0])
    print("도착역에서 가장 가까운 환승역 : "+ change[e_ch][0])
    shortest_path(s_ch)

    print("출발역에서 "+str(s_dis)+"만큼 가신 후 ", end="")
    path_list=[s_ch]
    while(path[e_ch]):
        path_list.insert(path[e_ch]%10)
        path[e_ch]=int(path[e_ch]/10)
    for i in path_list:
        print(change[i][0]+"역, ",end="")
    print("에서 환승하시면 됩니다.")
    print("총 "+str(s_dis+e_dis+distance[e_ch])+"정거장을 지났습니다.")


size=[800,582]
screen=pygame.display.set_mode(size)
pygame.display.set_caption("환승역 표시")


done =False
nowtime='selectCity'
clock=pygame.time.Clock()

base_m=pygame.image.load("map.jpg")

while done==False:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    screen.fill((255,255,255))#배경을 하얀색으로 채운다
    screen.blit(base_m,(0,0))
    
    for i in range(len(path_list)-1):
        if path_list[i]<path_list[i+1]:
            road=pygame.image.load(str(path_list[i])+str(path_list[i+1])+".PNG")
            screen.blit(road,(0,0))
        else:
            road=pygame.image.load(str(path_list[i+1])+str(path_list[i])+".PNG")
            screen.blit(road,(0,0))
    


    pygame.display.flip()
    clock.tick(20)

pygame.quit()
