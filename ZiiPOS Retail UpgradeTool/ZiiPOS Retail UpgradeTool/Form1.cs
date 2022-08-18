using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ZiiPOS_Retail_UpgradeTool
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        public class ZiiPOSRetailResponse
        {
            public DateTimeOffset Date { get; set; }
            public int TemperatureCelsius { get; set; }

        }
       
        private void upgradeButton_Click(object sender, EventArgs e)
        {
   
            String url = "https://wombat-api.ziicloud.com/api/vs/client-version/version?clientName=Zii.Retail_Classic&version=1";
            var jsoninfo ="";

            try
            {

                HttpWebRequest request = WebRequest.Create(url) as HttpWebRequest;
                HttpWebResponse response1 = (HttpWebResponse)request.GetResponse();
                request.Timeout = 10;
                WebHeaderCollection header = response1.Headers;

                var encoding = ASCIIEncoding.UTF8;
                //using (var reader = new System.IO.StreamReader(response.GetResponseStream(), encoding))
                using (var reader = new System.IO.StreamReader(response1.GetResponseStream(), encoding))
                {
                    string responseText = reader.ReadToEnd();
                    jsoninfo = responseText;
                    dynamic dyn = JsonConvert.DeserializeObject(jsoninfo);



                

                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.StackTrace.ToString());
                //Console.WriteLine(ex.StackTrace.ToString());
            }


        }



    }
}
