using Blog.Entities.Repositories;
using Blog.Utilities;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace Blog.Web.Areas.Admin.Controllers
{
    [Area("Admin")]
    [Authorize(Roles = $"{SD.AdminRole},{SD.EditorRole}")]
    public class ForumTopicController : Controller
    {
        private readonly IUnitOfWork _unitOfWork;

        public ForumTopicController(IUnitOfWork unitOfWork)
        {
            _unitOfWork = unitOfWork;
        }
        public IActionResult Index()
        {
            var forumtopic = _unitOfWork.ForumTopic.GetAll(Includeword: "ApplicationUser");
            return View(forumtopic);
        }

        [HttpPost]
        public IActionResult Delete(int id)
        {
            var forumtopic = _unitOfWork.ForumTopic.GetFirstorDefault(c => c.Id == id);
            if (forumtopic == null)
            {
                return NotFound();
            }

            _unitOfWork.ForumTopic.Remove(forumtopic);
            _unitOfWork.Complete();
            return RedirectToAction(nameof(Index));
        }
    }
}
