using Blog.Entities.Repositories;
using Microsoft.AspNetCore.Mvc;
using X.PagedList;

namespace Blog.Web.Areas.Forum.Controllers
{
    [Area("Forum")]
    public class HomeController : Controller
    {
        private readonly IUnitOfWork _unitOfWork;
        public HomeController(IUnitOfWork unitOfWork)
        {
            _unitOfWork = unitOfWork;
        }
        public IActionResult Index(int? page)
        {
            var PageNumber = page ?? 1;
            int PageSize = 6;

            var Forums = _unitOfWork.ForumTopic
                .GetAll(Includeword: "ApplicationUser")
                .OrderByDescending(x => x.CreatedAt)
                .ToPagedList(PageNumber, PageSize);

            return View(Forums);
        }


        public IActionResult GetForum(int? id) 
        {
            if(id == null || id <= 0)
            {
                return NotFound();
            }

            var Forum = _unitOfWork.ForumTopic.GetFirstorDefault(x => x.Id == id, Includeword : "Replies,ApplicationUser,Replies.ApplicationUser");
            if (Forum == null)
            {
                return NotFound();
            }
            return View(Forum);
        }



    }
}
