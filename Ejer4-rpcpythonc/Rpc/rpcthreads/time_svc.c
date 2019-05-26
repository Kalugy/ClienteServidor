#include <stdio.h>

		#include <rpc/rpc.h>
		#include "sync.cpp"
		//#include <thread.h>
		#include <pthread.h>
		#include "time_prot.h"
 
		void time_prog();
 
		void main(argc, argv)
		int argc;
		char *argv[];
		{
		int transpnum;
		char *nettype;
		int mode = RPC_SVC_MT_AUTO;
		int max = 20;      /* Set maximum number of threads to 20 */
 
		if (argc > 2) {
			fprintf(stderr, "usage: %s [nettype]\n", argv[0]);
			exit(1);
		}
 
		if (argc == 2)
			nettype = argv[1];
		else
			nettype = "netpath";
 
		if (!rpc_control(RPC_SVC_MTMODE_SET, &mode)) {
			printf("RPC_SVC_MTMODE_SET: failed\n");
			exit(1);
		}
		if (!rpc_control(RPC_SVC_THRMAX_SET, &max)) {
			printf("RPC_SVC_THRMAX_SET: failed\n");
			exit(1);
		}
		transpnum = svc_create( time_prog, TIME_PROG, TIME_VERS,
 			nettype);
 
		if (transpnum == 0) {
			fprintf(stderr, "%s: cannot create %s service.\n",
			argv[0], nettype);	
			exit(1);
		}
		svc_run();
	}
 
	/*
	 * The server dispatch function.
	 * The RPC server library creates a thread which executes
 * the server dispatcher routine time_prog().  After which
 * the RPC library destroys the thread.
 */
 
	static void
	time_prog(rqstp, transp)
		struct svc_req *rqstp;
		SVCXPRT *transp;
	{
 
		switch (rqstp->rq_proc) {
			case NULLPROC:
				svc_sendreply(transp, xdr_void, NULL);
				return;
			case TIME_GET:
				dotime(transp);
				break;
			default:
				svcerr_noproc(transp);
				return;
		}
	}
	dotime(transp)
	SVCXPRT *transp;
	{
	
		struct timev rslt;
		time_t thetime;
	
		thetime = time((time_t *)0);
		rslt.second = thetime % 60;
		thetime /= 60;
		rslt.minute = thetime % 60;
		thetime /= 60;
		rslt.hour = thetime % 24;
	if (!svc_sendreply(transp, xdr_timev,(caddr_t) &rslt)) {
			svcerr_systemerr(transp);
		}
	} 