using Blog.DataAccess.Data;
using Blog.Entities.Models;
using Blog.Entities.Repositories;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Blog.DataAccess.Implementation
{
    public class ForumTopicRepository : GenericRepository<ForumTopic>, IForumTopicRepository
    {
        private readonly AppDbContext _context;
        public ForumTopicRepository(AppDbContext context) : base(context)
        {
            _context = context;
        }
    }
}
