using HtmlAgilityPack;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Blog.Utilities
{
    public static class HtmlHelpers
    {
        public static string StripHtml(string html)
        {
            if (string.IsNullOrWhiteSpace(html)) return string.Empty;

            var doc = new HtmlDocument();
            doc.LoadHtml(html);

            // Extract plain text from the document
            return doc.DocumentNode.InnerText;
        }
    }
}
