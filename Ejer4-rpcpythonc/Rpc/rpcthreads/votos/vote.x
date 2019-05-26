const MAXMSG=1000;

typedef char line[MAXMSG];
typedef line *lineptr;


struct args1{
	int candidate;
	int myid;
};

typedef struct args1 ARGS1;

struct args2{
	int numofcandidates;
	char candidatelist[1024];
};

typedef struct args2 ARGS2;
	
program VOTE_SYSTEM{
	version one{
		lineptr Results(void)=1;
		int Vote(ARGS1)=2;
		ARGS2 Candidates(void)=3;
	}=1;
}=0x2000001;