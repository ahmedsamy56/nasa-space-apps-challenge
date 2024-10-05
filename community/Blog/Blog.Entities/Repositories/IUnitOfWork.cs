using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Blog.Entities.Repositories
{
    public interface IUnitOfWork : IDisposable
    {
        IApplicationUserRepository ApplicationUser { get; }   
        ICommentRepository Comment { get; }
        ICategoryRepository Category { get; }
        IPostRepository Post { get; }
        IForumTopicRepository ForumTopic { get; }
        IForumReplyRepository ForumReply { get; }
        int Complete();
    }
}
