using Blog.Entities.Models;
using Blog.Entities.Repositories;
using Blog.Utilities;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace Blog.Web.Areas.Admin.Controllers
{
    [Area("Admin")]
    [Authorize(Roles = $"{SD.AdminRole},{SD.EditorRole}")]
    public class ForumReplyController : Controller
    {
        private readonly IUnitOfWork _unitOfWork;

        public ForumReplyController(IUnitOfWork unitOfWork)
        {
            _unitOfWork = unitOfWork;
        }
        public IActionResult Index()
        {
            var ForumReply = _unitOfWork.ForumReply.GetAll(Includeword: "ApplicationUser,ForumTopic");
            return View(ForumReply);
        }

        [HttpPost]
        public IActionResult Delete(int id)
        {
            var forumreply = _unitOfWork.ForumReply.GetFirstorDefault(c => c.Id == id);
            if (forumreply == null)
            {
                return NotFound();
            }

            _unitOfWork.ForumReply.Remove(forumreply);
            _unitOfWork.Complete();
            return RedirectToAction(nameof(Index));
        }
    }
}
