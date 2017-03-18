#include<stdio.h>
#include<conio.h>

void main()
{
	int date, month;
	printf("Enter the Date of Birth and the Month Number : ");
	scanf("%d %d",&date,&month);
	
	if (((date>=22)  && (month==1)) || ((date<=18 ) && (month==2 )))
		printf("You are a AQUARIUS and yoour Birthstone is GARNET");
	if (((date>=19)  && (month==2)) || ((date<=20 ) && (month==3 )))
		printf("You are a PISCES and yoour Birthstone IS AMETHYST");
	if (((date>=21)  && (month==3)) || ((date<=20 ) && (month==4 )))
		printf("You are a ARIES and yoour Birthstone is BLOODSTONE");
	if (((date>=21)  && (month==4)) || ((date<=21 ) && (month==5 )))
		printf("You are a TAURUS and yoour Birthstone is SAPPHIRE");
	if (((date>=22)  && (month==5)) || ((date<=21 ) && (month==6 )))
		printf("You are a GEMINI and yoour Birthstone is AGATE");
	if (((date>=22)  && (month==6)) || ((date<=22 ) && (month==7 )))
		printf("You are a CANCER and yoour Birthstone is EMERALD");
	if (((date>=23)  && (month==7)) || ((date<=22 ) && (month==8 )))
		printf("You are a LEO and yoour Birthstone is ONYX");
	if (((date>=23)  && (month==8)) || ((date<=22 ) && (month==9 )))
		printf("You are a VIRGO and yoour Birthstone is CARNELIAN");
	if (((date>=23)  && (month==9)) || ((date<=23 ) && (month==10 )))
		printf("You are a LIBRA and yoour Birthstone is CHRYSOLITE");
	if (((date>=24)  && (month==10)) || ((date<=21 ) && (month==11 )))
		printf("You are a SCORPIO and yoour Birthstone is BERYL");
	if (((date>=22)  && (month==11)) || ((date<=21 ) && (month==12 )))
		printf("You are a SAGITTARIUS and yoour Birthstone is TOPAZ");
	if (((date>=22)  && (month==12)) || ((date<=21 ) && (month==1 )))
		printf("You are a CAPRICORN and yoour Birthstone is RUBY");
	
	getch();
}
