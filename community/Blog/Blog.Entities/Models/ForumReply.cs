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
    public class ForumReply
    {
        [Key]
        public int Id { get; set; }
        public string Content { get; set; }
        public DateTime CreatedAt { get; set; } = DateTime.Now;

        [ForeignKey(nameof(ForumTopic))]
        public int ForumTopicId { get; set; }
        [ValidateNever]
        public ForumTopic ForumTopic { get; set; }

        [ForeignKey(nameof(applicationUser))]
        [ValidateNever]
        public string applicationUserId { get; set; }
        [ValidateNever]
        public applicationUser ApplicationUser { get; set; }

        public int Upvotes { get; set; } = 0;
        public int Downvotes { get; set; } = 0;
    }
}
