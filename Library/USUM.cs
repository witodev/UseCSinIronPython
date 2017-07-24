using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Library
{
    public class USUM
    {
        public int id { get; set; }
        public float x { get; set; }
        public float y { get; set; }
        public float z { get; set; }

        public USUM()
        {
            id = 0;
            x = 0.0f;
            y = 0.0f;
            z = 0.0f;
        }

        public override string ToString()
        {
            return string.Format("{0,8}{1,12}{2,12}{3,12}", id, x, y, z);
        }
    }
}
