
using System.Collections.Generic;
using System.Text;

namespace Library
{
    public class FEM
    {
        public static Dictionary<int, USUM> SaveToFile(Dictionary<int, USUM> dic, string FilePath)
        {
            var sb = new StringBuilder();
            foreach (var item in dic)
            {
                var key = item.Key;
                var val = item.Value;

                sb.AppendLine(string.Format("{0,8}{1,12}{2,12}{3,12}", val.id, val.x, val.y, val.z));
            }

            System.IO.File.WriteAllText(FilePath, sb.ToString());

            return dic;
        }
    }
}