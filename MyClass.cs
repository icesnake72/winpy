using System;
namespace ex01
{
	public class MyClass
	{
		private int tot;
		private double avg;

        private int korea;
        private int english;
        private int mathmatics;
        private int science;


		public MyClass()
		{
			this.tot = 0;
			this.avg = 0;
		}

        public MyClass(int kor, int eng, int mathmatics, int science)
        {
            this.korea = kor;
            this.english = eng;
            this.mathmatics = mathmatics;
            this.science = science;
        }

        public int getTotal()
        {
            tot = korea + english + mathmatics + science;
            return tot;
        }

        public double getAverage()
        {
            return avg = getTotal() / 4.0;
        }
    }
}

