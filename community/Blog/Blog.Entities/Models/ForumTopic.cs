using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations.Schema;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc.ModelBinding.Validation;

namespace Blog.Entities.Models
{
    public class ForumTopic
    {
        [Key]
        public int Id { get; set; }
        public string Title { get; set; }
        public string Content { get; set; }
        public DateTime CreatedAt { get; set; } = DateTime.Now;

        [ForeignKey(nameof(applicationUser))]
        [ValidateNever]
        public string applicationUserId { get; set; }
        [ValidateNever]
        public applicationUser ApplicationUser { get; set; }
        [ValidateNever]
        public List<ForumReply>? Replies { get; set; } 
    }
}
