#include <rpc/types.h>

 
		struct timev {
			int second;

			int minute;
			int hour;
		};

 
		typedef struct timev timev;

		bool_t xdr_timev();
 
		#define TIME_PROG 0x40000001

		#define TIME_VERS 1
		#define TIME_GET 1